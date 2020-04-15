from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
import sys
from functools import partial
from PyQt5.QtCore import pyqtSlot
import requests

class Register(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Register Form'
        self.top = 450 - 150 
        self.left = 800 - 175
        self.width = 350
        self.height = 300

        self.newMain()

    def addAcc(self):
        print(self.inputUn.text())
        print(self.inputEm.text())
        print(self.inputPw.text())

        url = f"http://localhost?action=register&username={self.inputUn.text()}&email={self.inputEm.text()}&password={self.inputPw.text()}"

        result = requests.get(url)
        x = result.content.decode("utf-8")

        if(x == "SUCCESS"):
            return True
        else:
            print('Nije dodano')
            self.printUn.setText('ACCOUNT POSTOJI')
            self.printUn.setStyleSheet('QPushButton {background-color: red; color : black;}')
            return False
        
    def newMain(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.inputUn = QLineEdit(self)
        self.inputUn.move(20, 60)
        self.inputUn.resize(310, 35)
        self.inputUn.setPlaceholderText("Username")

        self.inputEm = QLineEdit(self)
        self.inputEm.move(20, 110)
        self.inputEm.resize(310, 35)
        self.inputEm.setPlaceholderText("Email")

        self.inputPw = QLineEdit(self)
        self.inputPw.move(20, 160)
        self.inputPw.resize(310, 35)
        self.inputPw.setPlaceholderText('Password')

        self.printUn = QPushButton('Register', self)
        self.printUn.move(20, 235)
        self.printUn.resize(310, 35)
        self.printUn.clicked.connect(self.addAcc)

        self.closeButton = QPushButton(self)
        self.closeButton.setProperty("cssClass", "closeButton")
        self.closeButton.resize(32, 32)
        self.closeButton.setIcon(QtGui.QIcon('x.png'))
        self.closeButton.setIconSize(QtCore.QSize(20, 20))
        self.closeButton.clicked.connect(self.close)
        self.closeButton.move(317, 1)

        self.content = open("registerForm.css", "r")
        self.setStyleSheet(self.content.read())

        self.inputUn.setAlignment(QtCore.Qt.AlignCenter)
        self.inputEm.setAlignment(QtCore.Qt.AlignCenter)
        self.inputPw.setAlignment(QtCore.Qt.AlignCenter)

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.show()

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    def mouseMoveEvent(self, event):
        if event.buttons() == QtCore.Qt.RightButton or event.buttons() == QtCore.Qt.LeftButton:            
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Register()
    sys.exit(app.exec_())