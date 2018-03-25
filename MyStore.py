# -*- coding: utf-8 -*-

"""
Module implementing SimpleExampleAction.
"""
import sys
import os
from datetime import date

import yagmail
from PyQt5.QtWidgets import QApplication, QMessageBox
from PyQt5.QtCore import pyqtSlot, QSortFilterProxyModel
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog
from PyQt5.QtSql import *

from Ui_SimplExample import Ui_Dialog

config_file = 'config.txt'
def read_conf(config_file):
    with open(config_file, 'r', encoding='utf-8') as cf:
        config_text = [e[1:].split("=") for e in cf.read().splitlines()
                       if e.startswith("#")
                       ]
        return dict(config_text)


def get_last_backup():
    back_backup_dir = read_conf(config_file).get("智慧记备份目录")
    file_list = [e for e in os.listdir(back_backup_dir) if e.endswith(".bak")]
    file_list.sort(key=lambda fn: os.path.getmtime(os.path.join(back_backup_dir, fn)))
    bak_file = os.path.join(back_backup_dir, file_list[-1])
    return bak_file

def sql_format(str):
    return ('"%' + str + '%"')

class SimpleExampleAction(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(SimpleExampleAction, self).__init__(parent)
        self.setupUi(self)
        
        
        db = QSqlDatabase.addDatabase("QSQLITE")
        backup_file = get_last_backup()
        db.setDatabaseName(backup_file)
        if db.open():
            print("数据库连接成功!")
            print("你现在操作的数据库是: %s" % backup_file)
       
    
    @pyqtSlot()
    def on_pushButton_backup_clicked(self):
        """
        Slot documentation goes here.
        
        # TODO: not implemented yet
        raise NotImplementedError
        """
        config = read_conf(config_file)
        host_adr = config.get("SMTP服务器地址")
        host_port = config.get("SMTP服务器端口")
        mailuser = config.get("邮箱用户")
        mailpass = config.get("邮箱密码")
        mailrev = config.get("邮件收件人")
        back_backup_dir = config.get("智慧记备份目录")
        last_backup = get_last_backup()
        att_back = os.path.join(back_backup_dir, last_backup)
        message = "确认要发送数据库备份文件:\n%s \n至邮箱:%s ?" % (last_backup, mailrev)
        reply = QMessageBox.information(self, "提示", message, QMessageBox.Yes | QMessageBox.No)
        if (reply == QMessageBox.Yes) :
            QMessageBox.information(self, "提示", "正在发送邮件,请稍候...")

            # 附件目录以数组形式存入
            atts = [att_back]

            mailsubject = "智慧记备份文件\n%s\n%s" % (str(date.today()), last_backup)
            yag = yagmail.SMTP(user=mailuser, password=mailpass, host=host_adr)
            yag.send(mailrev,
                     subject=mailsubject,
                     contents=mailsubject,
                     attachments=atts
                     )
            print("send mail sucess")
            QMessageBox.information(self, "提示", "发送邮件成功!")
        else:
            print("邮件发送失败!")
        

    @pyqtSlot()
    def on_pushButton_query_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        #raise NotImplementedError
        
        customer = self.lineEdit_cus.text()
        product = self.lineEdit_pro.text()

        self.model = QSqlQueryModel(self)

        argument = (sql_format(customer), sql_format(customer), sql_format(product), sql_format(product))
        sqlstr = "SELECT c.name, p.name, s.opt_on, s.code, sit.qty, sit.prc, sit.remark " \
             "FROM saleitems AS sit, sales AS s, companies AS c, products AS p " \
             "WHERE sit.is_del = 0 AND  s.id = sit.sale_id AND c.id = s.company_id " \
             "AND p.id = sit.product_id " \
             "AND (c.name LIKE %s OR c.pinyin LIKE %s) " \
             "AND (p.name like %s or p.pinyin like %s) " \
             "ORDER BY s.opt_on DESC" % argument
        print(sqlstr)
        
        self.model.setQuery(sqlstr)
        header = ['客户', '品名', '日期', '单号',  '数量', '单价/元', '备注']
        for i in range(len(header)):
            self.model.setHeaderData(i, Qt.Horizontal, header[i])

        self.proxyModel = QSortFilterProxyModel(self)
        self.proxyModel.setSourceModel(self.model)
        self.tableView.setSortingEnabled(True)
        self.tableView.setModel(self.proxyModel)
        self.tableView.setColumnWidth(0, 140)
        self.tableView.setColumnWidth(1, 180)
        self.tableView.setColumnWidth(2, 140)
        self.tableView.setColumnWidth(3, 180)
        self.tableView.setColumnWidth(4, 80)
        self.tableView.setColumnWidth(5, 80)
        self.tableView.setColumnWidth(6, 150)
        
        #self.tableView.resizeColumnsToContents()
           
    def on_pushButton_query_pro_clicked(self):
        customer = self.lineEdit_cus.text()
        product = self.lineEdit_pro.text()

        self.model = QSqlQueryModel(self)

        argument = (sql_format(customer), sql_format(customer), sql_format(product), sql_format(product))
        sqlstr = "SELECT cs.name AS 供货商, pro.name AS 品名, purs.opt_on AS 日期, purs.code AS 单号, " \
                 "pitems.qty AS 数量, pitems.prc AS 价格, pro.cur_stock AS 库存 " \
                 "FROM products AS pro, puritems AS pitems, purs AS purs, companies AS cs " \
                 "WHERE pro.id = pitems.product_id AND pitems.pur_id = purs.id " \
                 "AND pitems.is_del = 0 AND cs.id = purs.company_id " \
                 "AND (cs.name like %s OR cs.pinyin like %s) " \
                 "AND (pro.name like %s OR pro.pinyin like %s) " \
                 "ORDER BY 日期"% argument
        print(sqlstr)

        self.model.setQuery(sqlstr)
        header = ['供货商', '品名', '日期', '单号', '数量', '单价/元', '库存']
        for i in range(len(header)):
            self.model.setHeaderData(i, Qt.Horizontal, header[i])

        #用QSortFilterProxyModel对model进行排序
        self.proxyModel = QSortFilterProxyModel(self)
        self.proxyModel.setSourceModel(self.model)
        self.tableView.setSortingEnabled(True)
        self.tableView.setModel(self.proxyModel)

        self.tableView.setColumnWidth(0, 30)
        self.tableView.setColumnWidth(1, 200)
        self.tableView.setColumnWidth(2, 140)
        self.tableView.setColumnWidth(3, 180)
        self.tableView.setColumnWidth(4, 80)
        self.tableView.setColumnWidth(5, 80)
        self.tableView.setColumnWidth(6, 80)

if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    dlg = SimpleExampleAction()
    dlg.show()
    sys.exit(app.exec_())
    
