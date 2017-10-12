import Sensor_Stat as stat
from socket import *
from sys import exit
import time
#from data_file import SocketInfo


#Inputlist = [('ULTRA',ULTRA_value),('PIR',PIR_value),('TEMP',TEMP_value),('HUMI',TEMP_value),('ILLU',ILLU_value)]
#LCD = ('LCD', LCD_value)
#LED = ('LED',LED_value)
#PIEZO = ('PIEZO',PIEZO_value)
#FND = ('FND','ON',FND_value)
#MOTOR = ('MOTOR',MOTOR_value)
#JOY = ('JOY',JOY_value)


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
            self.s.send(str(stat.joy))
            self.s.send()
            self.s.send(str(stat.pir))
            self.s.send()
            self.s.send(str(stat.light))
            self.s.send()
            self.s.send(str(stat.ultra))
            self.s.send()
            #self.s.send(LCD[1])
            self.s.send(str(stat.temp))
            self.s.send()
            self.s.send(str(stat.humi))
            self.s.send()
            self.s.send(stat.lcd)
            self.s.send()
            self.s.send(stat.led1)
            self.s.send()
            self.s.send(stat.led2)
            self.s.send()
            #self.s.send(FND[1])
            self.s.send(stat.motor)
            self.s.send()
            s.close()

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
