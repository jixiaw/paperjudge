
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from mainWindow import *
from paperjudge import judge
from Datebase.datebase import DBHelper
import runPhoto1
import runPhoto2
from runPhoto1 import viewPhoto1
from runPhoto2 import viewPhoto2

class MyWindow(Ui_MainWindow,QMainWindow):
    def __init__(self,parent=None):
        super(MyWindow,self).__init__(parent)
        self.setupUi(self)
       
        palette1 = QPalette()
        # palette1.setColor(self.backgroundRole(), QColor(192,253,123))   # 设置背景颜色
        palette1.setBrush(self.backgroundRole(), QBrush(QPixmap('1.jpg'))) # 设置背景图片
        self.setPalette(palette1)
        self.setAutoFillBackground(True)

        self.select_dir.clicked.connect(self.openfile)
        self.correct.clicked.connect(self.correct_papers)
        self.select.clicked.connect(self.select_action)

        #查询
        self.action_5.setShortcut('Ctrl+R')
        self.action_5.triggered.connect(self.select_all)
        #批卷
        self.action_4.setShortcut('Ctrl+P')
        self.action_4.triggered.connect(self.correct_papers)
        #选择文件夹
        self.action_3.setShortcut('Ctrl+S')
        self.action_3.triggered.connect(self.openfile)
        #退出
        self.action.setShortcut('Ctrl+Q')
        self.action.setStatusTip('Exit application')
        self.action.triggered.connect(qApp.quit)



    def openfile(self):
        self.directory = QFileDialog.getExistingDirectory(self, "选择文件夹", "/")
        self.display_dir.setText(self.directory)
        print(self.directory)  # 打印文件夹路径


    def correct_papers(self):  # 批量批改
        imgpath1 = ''
        imgpath2 = ''
        num = ''
        min = 123
        max = 127
        for i in range(min, max, 2):
            num = '' + str(i)
            num = num.zfill(5)
            imgpath1 = 'photos/Image_' + num + '.jpg'
            num = '' + str(i + 1)
            num = num.zfill(5)
            imgpath2 = 'photos/Image_' + num + '.jpg'
            text = "当前正在批改第"+str(int((i-min)/2+1))+"张，共"+str(int((max-min)/2))+"张"
            self.remind.setText(text)
            QtWidgets.QApplication.processEvents()
            print(imgpath1, imgpath2)
            judge(imgpath1, imgpath2)
        msg_box = QtWidgets.QMessageBox.information(self, '提示', '批改完成')

    def select_action(self):   #查询
        dbhelper = DBHelper()
        _, grade, fpath, bpath = dbhelper.search_data(self.inputID.text())
        print(grade)
        line = "该同学的成绩为:"+str(grade)
        self.result.setText(line)
        runPhoto1.p1.viewP(fpath)
        runPhoto2.p2.viewP(bpath)
        runPhoto1.p1.show()
        runPhoto2.p2.show()
        
        print(self.inputID.text())

    def select_all(self): # 查询全部学生
        mydb = DBHelper()

        result = mydb.search_all()
        self.tableWidget.setRowCount(62)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setHorizontalHeaderLabels(['学号', '成绩'])
        newItem1 = QTableWidgetItem("130122")
        self.tableWidget.setItem(0,0,newItem1)
        newItem1 = QTableWidgetItem("130")
        self.tableWidget.setItem(0, 1, newItem1)
        i = 0
        for row in result:
            newItem1 = QTableWidgetItem(row[0])
            self.tableWidget.setItem(i , 0 , newItem1)
            newItem2 = QTableWidgetItem(str(row[1]))
            self.tableWidget.setItem(i , 1 , newItem2)
            i=i+1
            
'''
        self.select_paper.clicked.connect(self.openimage)
        self.select_paper_2.clicked.connect(self.openimage2)
        self.select_dir.clicked.connect(self.openfile)
        self.correct.clicked.connect(self.correct_paper)
        self.correct_more.clicked.connect(self.correct_papers)

    def openimage(self):#打开试卷正面图片
        self.imgName1, imgType = QFileDialog.getOpenFileName(self, '选择图片', '/', 'Image files(*.jpg *.gif *.png)')
        print(self.imgName1)
        jpg = QtGui.QPixmap(self.imgName1).scaled(self.label.width(), self.label.height())
        self.label.setPixmap(jpg)
    def openimage2(self):#打开试卷背面图片
        self.imgName2, imgType = QFileDialog.getOpenFileName(self, '选择图片', '/', 'Image files(*.jpg *.gif *.png)')
        print(self.imgName2)
        jpg = QtGui.QPixmap(self.imgName2).scaled(self.label_2.width(), self.label_2.height())
        self.label_2.setPixmap(jpg)


    def correct_paper(self):#批改一张
        print(self.imgName1)
        print(self.imgName2)
        msg_box = QtWidgets.QMessageBox.information(self, '提示', '批改完成')


    def openfile(self):
        self.directory = QFileDialog.getExistingDirectory(self, "选择文件夹", "/")
        print(self.directory)  # 打印文件夹路径

    def correct_papers(self):#批量批改
        print(self.directory)
        msg_box = QtWidgets.QMessageBox.information(self, '提示', '批改完成')
'''


if __name__ == '__main__':
    import  sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MyWindow()
    runPhoto1.p1=viewPhoto1()
        
    runPhoto2.p2=viewPhoto2()
    MainWindow.show()
    sys.exit(app.exec_())