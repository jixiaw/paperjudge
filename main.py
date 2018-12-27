
import login
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QLineEdit,QDialog
from login import Ui_Dialog
from runMainWindow import MyWindow

class myLogin(Ui_Dialog,QDialog):
    def __init__(self):
        super(myLogin,self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.password.setEchoMode(QLineEdit.Password)
        self.pushButton_2.clicked.connect(self.close)
        self.pushButton.clicked.connect(self.login)

    def login(self):
        if self.username.text() == 'admin' and self.password.text() == '123456':
            self.accept()
        else:
            msg_box = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Critical, 'Error', '用户名密码错误', parent=self)
            msg_box.exec_()


def check_login():
    #login_dialog = QtWidgets.QDialog()
    ui = myLogin()
    #ui.setupUi(login_dialog)
    ui.show()
    #login_dialog.show()
    responce = ui.exec_()
    if responce == QtWidgets.QDialog.Accepted:
        return True
    else:
        return False

def main():
    app = QtWidgets.QApplication(sys.argv)
    if check_login():
        #MainWindow = QtWidgets.QMainWindow()
        ui = MyWindow()
        ui.show()
        sys.exit(app.exec_())


if __name__ == '__main__':
    main()