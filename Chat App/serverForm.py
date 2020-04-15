import socket
import time
import threading
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import pyqtSlot
import mysql.connector
import sys
from datetime import datetime
from datetime import date

'''
users = {}

hs = 256

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
s.bind(("127.0.0.1", 5522))
s.listen(5)

def Listen(socket):
    while True:
        clientMessage = socket.recv(1024).decode("utf-8")
        if (len(clientMessage) <= 0):
             print('Server je ugasen. ')
             break

        addr = f"{socket.getpeername()[0]}:{socket.getpeername()[1]}"

        if (len(users[addr]) == 0):
            users[str(addr)] = clientMessage                                                                                                            
            print(f"{clientMessage} je usao.")
        else:
            print(f"{users[addr]}>> {clientMessage}")

while True:
    clientSocket, address = s.accept()
    
    clientSocket.send(bytes("Welcome to the chat room! ", "utf-8"))

    users[f"{clientSocket.getpeername()[0]}:{clientSocket.getpeername()[1]}"] = "" # to je to,

    nesto = threading.Thread(target = Listen, args = (clientSocket,))
    nesto.start()
    print(f'Connection from {address} has been established!')

'''


class ServerSocket():
    def __init__(self):
        #super().__init__(self)
        self.title = "Server"
        self.top = 400
        self.left = 400
        self.width = 350
        self.height = 200

        self.users = {}
        self.connected = []

        self.loadChat = open("chat.txt", "r")
        self.allChat = self.loadChat.read().split("\n")

        self.createServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.createServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
        self.createServer.bind(("localhost", 5522))
        self.createServer.listen(5)
        self.initSocket()

    def ServerListen(self, socket):
        try:
            while True:
                clientMessage = socket.recv(1024).decode("utf-8")

                if(len(clientMessage) <= 0):
                    break
                
                ServerAddress = f"{socket.getpeername()[0]}:{socket.getpeername()[1]}"
                if (len(self.users[ServerAddress]) == 0):
                    self.users[str(ServerAddress)] = clientMessage                                                                                                            
                    print(f"{clientMessage} je usao.")
                    self.connected.append(socket)
                    self.sendChat(socket)
                else:
                    print(f"{self.users[ServerAddress]} >> {clientMessage}")
                    self.chatFile = open("chat.txt", "a")
                    self.Broadcast(socket, clientMessage)
                    self.chatFile.write(f"{self.users[ServerAddress]} >> {clientMessage}" + '\n')
                    self.chatFile.close()
                    self.allChat.append(f"{self.users[ServerAddress]} >> {clientMessage}")
        except:
            print(f'neko je izaso otac ga jebo : {self.users[ServerAddress]}')
            now = datetime.now()
            date_time = now.strftime("%H:%M:%S")
            # uzas = datetime.today() + " " + datetime.now().strftime("%H:%M:%S")
            self.chatFile = open("chat.txt", "a")
            #self.chatFile.write(f"[USER ({self.users[ServerAddress]}) LEFT] : {date.today()} {date_time}")
            self.chatFile.close()
            self.users.pop(ServerAddress)
            self.connected.remove(socket)

    def initSocket(self):
        while True:
            self.clientSocket, self.address = self.createServer.accept()
    
            self.clientSocket.send(bytes("Welcome to the chat room!", "utf-8"))

            self.users[f"{self.clientSocket.getpeername()[0]}:{self.clientSocket.getpeername()[1]}"] = "" # to je to,

            self.nesto = threading.Thread(target = self.ServerListen, args = (self.clientSocket,))
            self.nesto.start()
            print(f'Connection from {self.address} has been established!')

    def Broadcast(self, sender, message):
        print("Broadcast start")
        for i in range(len(self.connected)):
            self.connected[i].send(bytes(self.users[f"{sender.getpeername()[0]}:{sender.getpeername()[1]}"] + ' >> ' + message, "utf-8"))
            print(f"Poslo sam poruku: {self.connected[i].getpeername()[0]}:{self.connected[i].getpeername()[1]}: {message}")
        print("Broadcast end")

    def sendChat(self, socket):
        for message in self.allChat:
            time.sleep(0.1)
            socket.send(bytes(message, "utf-8"))
        
if __name__ == "__main__":
    ServerSocket()