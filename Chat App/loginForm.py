from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
import sys
from functools import partial
from serverForm import *
from clientForm import *
import requests

class Login(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Login Form'
        self.top = 450 - 150 
        self.left = 800 - 175
        self.width = 350
        self.height = 300
        self.mainDef()

    def checkUser(self):
        url = f"http://localhost?action=login&username={self.inputUn.text()}&password={self.userUn.text()}"

        x = requests.get(url)
        result = x.content.decode("utf-8")

        print(x.status_code)
        print(result)
        
        if(result == "SUCCESS"):
            return 1
        else:
            return 2

    def nesto(self):
        print(self.inputUn.text() + ' : ' + self.userUn.text())

        if(self.checkUser() == 1):
            self.result.setText('Uspjesno si logovan')
            self.result.setStyleSheet("QLabel {color: green;}")

            self.close()
            self.openClientForm = ClientSocket()
            self.openClientForm.Connect(self.inputUn.text())
        
        if(self.checkUser() == 2):
            self.result.setText('Provjeri podatke ponovo')
            self.result.setStyleSheet('QLabel {color: red;}')

    def mainDef(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.welcome = QLabel(self)
        self.welcome.setText('Login')
        self.welcome.setAlignment(QtCore.Qt.AlignCenter)
        self.welcome.move(20, 4)
        self.welcome.resize(310, 30)

        design = open("loginForm.css", "r")
        self.setStyleSheet(design.read())
        design.close()

        self.inputUn = QLineEdit(self)
        self.inputUn.move(20, 80)
        self.inputUn.setAlignment(QtCore.Qt.AlignCenter)
        self.inputUn.resize(310, 35)
        self.inputUn.setPlaceholderText('Username')

        self.userUn = QLineEdit(self)
        self.userUn.move(20, 132)
        self.userUn.setAlignment(QtCore.Qt.AlignCenter)
        self.userUn.resize(310, 35)
        self.userUn.setPlaceholderText('Password')

        self.printUn = QPushButton('Login', self)
        self.printUn.move(20, 200)
        self.printUn.resize(310, 35)
        self.printUn.clicked.connect(self.nesto)

        self.result = QLabel(self)
        self.result.setAlignment(QtCore.Qt.AlignCenter)
        self.result.move(20, 252)
        self.result.resize(310, 30)
        self.result.setText('')

        self.closeButton = QPushButton(self)
        self.closeButton.setProperty("cssClass", "closeButton")
        self.closeButton.resize(32, 32)
        self.closeButton.setIcon(QtGui.QIcon('x.png'))
        self.closeButton.setIconSize(QtCore.QSize(20, 20))
        self.closeButton.clicked.connect(self.close)
        self.closeButton.move(317, 1)

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Login()
    sys.exit(app.exec_())
