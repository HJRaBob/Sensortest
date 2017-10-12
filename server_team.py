import socket
#import sys
import RPi.GPIO as GPIO 
from time import sleep
#import GUIserver as mylib
#import pymysql

class Socket:
    def __init__(self, data):

        self.svrsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.svrsock.bind(('70.12.114.181', 8001))
        self.svrsock.listen(0)


        self.clientsock, addr = svrsock.accept()
        self.data = clientsock.recv(65535)
        self.bdsock.send(data)

        print(data.decode())
        print(addr[0], addr[1])

        while True:
            data = conn.recv(1024)
            if not data: break
            conn.send(data)
        conn.close()


    def split(data):
        words = data.split()
            print(words)









            
#connect = pymysql.connect(db='data_base')
#curs = connect.cursor()
#data = (('JOG_ON', 1, 'JOG'), ('JOG_OFF', 0, 'JOG'),
#        ('LED_ON', 1, 'LED'), ('LED_OFF', 0, 'LED')
#        ('MOTOR_ON', 1, 'MOTOR'), ('MOTOR_OFF', 0, 'MOTOR')
#        ('PIR_ON', 1, 'PIR'), ('PIR_OFF', 0, 'PIR')
#        ('ILLU_ON', 1, 'ILLU'), ('ILLU_OFF', 0, 'ILLU')
#        ('TEMP_ON', 1, 'TEMP'), ('TEMP_OFF', 0, 'TEMP')
#        ('PIEZO_ON', 1, 'PIEZO'), ('PIEZO_OFF', 0, 'PIEZO')
#        ('SONIC_ON', 1, 'SONIC'), ('SONIC_OFF', 0, 'SONIC'))
#sql = """insert into data() values (%s, %s)"""
#curs.execute(sql, data)
#Socket(data)
#curs.execute("insert into values ('table_name, :state);" (table_name, state))
#state = [('JOG', 54), ('LED', 34), ('MOTOR', 44), ('PIR', ), ('ILLU', ),
#          ('TEMP', ), ('PIEZO', ), ('SONIC', )]
#curs.executemany('insert into employee values(?,?)', values)

#connect.commit()
#connect.close()

#    def send(self):

#    def data(self):
#        LED
#        LCD
#        PIEZO
#        MOTOR
