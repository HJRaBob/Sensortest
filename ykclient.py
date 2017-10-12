import
from socket import *
from sys import exit
import time
#from data_file import SocketInfo


Inputlist = [('ULTRA',ULTRA_value),('PIR',PIR_value),('TEMP',TEMP_value),('HUMI',TEMP_value),('ILLU',ILLU_value)]
LCD = ('LCD', LCD_value)
LED = ('LED',LED_value)
PIEZO = ('PIEZO',PIEZO_value)
FND = ('FND','ON',FND_value)
MOTOR = ('MOTOR',MOTOR_value)
JOY = ('JOY',JOY_value)


class SocketInfo :

    def __init__(self):
        self.HOST = 'localhost'
        self.PORT = 8001
        self.BUFSIZE = 1024
        self.ADDR = (HOST, PORT)
        #self.csock.connect(('70.12.114.169',8001))
        self.s = socket.socket(AF_INET,SOCK_STREAM)

    #def master_recieve(self):

    def send(self):
        while True:
            self.s.send(Inputlist[0][1])
            self.s.send(Inputlist[1][1])
            self.s.send(Inputlist[2][1])
            self.s.send(Inputlist[3][1])
            self.s.send(LCD[1])
            self.s.send(LED[1])
            self.s.send(PIEZZO[1])
            self.s.send(MOTOR[1])
            self.s.send(FND[1])
            self.s.send(JOY[1])


            s.close()

class Sensor_State:

    def __init__(self):
        #input
        self.stat_joy
        self.stat_pir
        self.stat_led
        self.stat_ultra
        self.stat_temp
        self.stat_humi
        #output
        self.stat_lcd
        self.stat_led
        self.stat_piezo
        self.stat_fnd
        self.stat_motor
    def state_joy(self):
        self.stat_
#while True:
#    try:
#        commend = raw_input(">>")
#        s.send(list)
#        commend = s.recv(SocketInfo.BUFSIZE)

#    except Exception as e:
#        print "%s:%s" %(e,SocketInfo.ADDR)
#        s.close()
#        exit()
#        print "connet is success"
