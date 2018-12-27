# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtGui import QIcon
class Ui_Dialog(object):

    def setupUi(self, Dialog):
       # self.Dialog=Dialog
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)

        Dialog.setWindowIcon(QIcon('logo.png'))
        Dialog.setStyleSheet("background-image:url(Background.jpg)")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(130, 20, 181, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(70, 90, 54, 12))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(70, 130, 54, 12))
        self.label_3.setObjectName("label_3")
        self.username = QtWidgets.QLineEdit(Dialog)
        self.username.setGeometry(QtCore.QRect(150, 90, 113, 20))
        self.username.setText("")
        self.username.setObjectName("username")
        self.password = QtWidgets.QLineEdit(Dialog)
        self.password.setEnabled(True)
        self.password.setGeometry(QtCore.QRect(150, 130, 113, 20))
        self.password.setText("")
        self.password.setObjectName("password")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(80, 190, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(200, 190, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        #self.pushButton_2.clicked.connect(Dialog.close)
        #self.pushButton.clicked.connect(self.login)





    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "自动批卷系统"))
        self.label_2.setText(_translate("Dialog", "用户名"))
        self.label_3.setText(_translate("Dialog", "密码"))
        self.username.setPlaceholderText(_translate("Dialog", "username"))
        self.password.setPlaceholderText(_translate("Dialog", "password"))
        self.pushButton.setText(_translate("Dialog", "登录"))
        self.pushButton_2.setText(_translate("Dialog", "取消"))
        self.setWindowTitle(_translate("Dialog", "登录窗口"))


