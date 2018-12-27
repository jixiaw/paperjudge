# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWin.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


from picture2 import *


global p2
class viewPhoto2(Ui_photo2, QMainWindow):
    
    def __init__(self):
        super(viewPhoto2,self).__init__()
        self.setupUi(self)
    def viewP(self,name):
        self.label.setPixmap(QtGui.QPixmap(name).scaled(self.label.width(), self.label.height()))

