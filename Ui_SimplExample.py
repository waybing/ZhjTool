# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SimplExample.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1113, 785)
        font = QtGui.QFont()
        font.setPointSize(16)
        Dialog.setFont(font)
        Dialog.setSizeGripEnabled(True)
        self.pushButton_backup = QtWidgets.QPushButton(Dialog)
        self.pushButton_backup.setGeometry(QtCore.QRect(940, 30, 151, 51))
        self.pushButton_backup.setObjectName("pushButton_backup")
        self.pushButton_query_sale = QtWidgets.QPushButton(Dialog)
        self.pushButton_query_sale.setGeometry(QtCore.QRect(620, 30, 121, 51))
        self.pushButton_query_sale.setObjectName("pushButton_query_sale")
        self.tableView = QtWidgets.QTableView(Dialog)
        self.tableView.setGeometry(QtCore.QRect(30, 110, 1061, 621))
        self.tableView.setObjectName("tableView")
        self.splitter = QtWidgets.QSplitter(Dialog)
        self.splitter.setGeometry(QtCore.QRect(30, 30, 571, 51))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.label = QtWidgets.QLabel(self.splitter)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.lineEdit_cus = QtWidgets.QLineEdit(self.splitter)
        self.lineEdit_cus.setObjectName("lineEdit_cus")
        self.label_2 = QtWidgets.QLabel(self.splitter)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.lineEdit_pro = QtWidgets.QLineEdit(self.splitter)
        self.lineEdit_pro.setObjectName("lineEdit_pro")
        self.pushButton_query_pur = QtWidgets.QPushButton(Dialog)
        self.pushButton_query_pur.setGeometry(QtCore.QRect(760, 30, 161, 51))
        self.pushButton_query_pur.setObjectName("pushButton_query_pur")
        self.pushButton_send_shortcut = QtWidgets.QPushButton(Dialog)
        self.pushButton_send_shortcut.setGeometry(QtCore.QRect(30, 740, 271, 31))
        self.pushButton_send_shortcut.setObjectName("pushButton_send_shortcut")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.lineEdit_cus, self.lineEdit_pro)
        Dialog.setTabOrder(self.lineEdit_pro, self.pushButton_query_sale)
        Dialog.setTabOrder(self.pushButton_query_sale, self.pushButton_query_pur)
        Dialog.setTabOrder(self.pushButton_query_pur, self.pushButton_backup)
        Dialog.setTabOrder(self.pushButton_backup, self.tableView)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "销售单历史查询"))
        self.pushButton_backup.setText(_translate("Dialog", "备份到邮箱"))
        self.pushButton_query_sale.setText(_translate("Dialog", "出货查询"))
        self.label.setText(_translate("Dialog", "姓名:"))
        self.label_2.setText(_translate("Dialog", "商品:"))
        self.pushButton_query_pur.setText(_translate("Dialog", "进货查询"))
        self.pushButton_send_shortcut.setText(_translate("Dialog", "发送快捷方式到桌面"))

