import socket
#import sys
#import RPi.GPIO as GPIO
from time import sleep
#import GUIserver as mylib
#import pymysql

class Socket:
    def __init__(self):

        HOST='192.168.101.120'
        PORT=5800
        self.svrsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.svrsock.bind((HOST, PORT))
        self.svrsock.listen(0)
#        self.svrsock.connect(HOST, PORT)


        conn, addr = self.svrsock.accept()
        self.data = conn.recv(65535)

        # print(self.data.decode())
        # print(addr[0], addr[1])

        # while True:
        #     self.data = conn.recv(1024)
        #     print(self.data)
        #     if not self.data: break
        #     conn.send(self.data)
        # conn.close()


    def split_word(self):
        words = self.data.split()
        print(words)

test = Socket()
while True:
    test.split_word()
