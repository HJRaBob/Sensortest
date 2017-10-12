import socket
#import sys
#import RPi.GPIO as GPIO 
from time import sleep
#import GUIserver as mylib
#import pymysql

class Socket:
    def __init__(self, data):

        HOST='localhost'
        PORT=8001
        self.svrsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.svrsock.bind(('HOST', PORT))
        self.svrsock.listen(5)
        self.svrsock.connect('HOST', PORT)


        conn, addr = svrsock.accept()
        data = clientsock.recv(65535)
        clientsock.send(data)

        print(data.decode())
        print(addr[0], addr[1])

        while True:
            data = conn.recv(1024)
            print(data)
            if not data: break
            conn.send(data)
        conn.close()


    def split_word(data):
        words = data.split()
        print(words)
