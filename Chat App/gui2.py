from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
import sys
from PyQt5.QtCore import pyqtSlot
from loginForm import *
from registerForm import *

class App(QMainWindow):
    def loginForm(self):
        self.close()
        self.newApp = Login()

    def registerForm(self):
        self.close()
        self.app = Register()

    def __init__(self):
        super().__init__()
        self.title = 'Login and Register'

        self.top = 450 - 150 
        self.left = 800 - 175
        self.width = 350
        self.height = 300
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.loginButton = QPushButton('Login', self)
        self.loginButton.setToolTip('Nemam pojma cijeli dan')
        self.loginButton.move(20, 70)
        self.loginButton.resize(310, 40)
        self.loginButton.clicked.connect(self.loginForm)

        self.registerButton = QPushButton('Register', self)
        self.registerButton.setToolTip('Nemam pojma cijeli dan')
        self.registerButton.move(20, 120)
        self.registerButton.resize(310, 40)
        self.registerButton.clicked.connect(self.registerForm)

        self.infoButton = QPushButton("", self)
        self.infoButton.resize(32, 32)
        self.infoButton.move(350 - 33, 300 - 33)

        self.closeButton = QPushButton(self)
        self.closeButton.setProperty("cssClass", "closeButton")
        self.closeButton.resize(32, 32)
        self.closeButton.setIcon(QtGui.QIcon('x.png'))
        self.closeButton.setIconSize(QtCore.QSize(20, 20))
        self.closeButton.clicked.connect(self.close)
        self.closeButton.move(350 - 33, 1)

        cssFile = open("gui2.css", "r")
        self.setStyleSheet(cssFile.read())

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = App()
    sys.exit(app.exec_())