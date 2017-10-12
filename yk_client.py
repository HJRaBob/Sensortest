import Sensor_Stat as stat
import socket
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
        self.HOST = '192.168.101.120'
        self.PORT = 5800
        # self.BUFSIZE = 1024
        self.ADDR = (self.HOST, self.PORT)
        self.s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.s.connect(self.ADDR)

    #def master_recieve(self):
    def send(self,cla):
        self.s.send(str(cla.stat_joy).encode())
        self.s.send(" ".encode())
        self.s.send(str(cla.stat_pir).encode())
        self.s.send(" ".encode())
        self.s.send(str(cla.stat_light).encode())
        self.s.send(" ".encode())
        self.s.send(str(cla.stat_ultra).encode())
        self.s.send(" ".encode())
        #self.s.send(LCD[1])
        self.s.send(str(cla.stat_temp).encode())
        self.s.send(" ".encode())
        self.s.send(bytes(cla.stat_humi).encode())
        self.s.send(" ".encode())
        self.s.send(bytes(cla.stat_lcd).encode())
        self.s.send(" ".encode())
        self.s.send(bytes(cla.stat_led1).encode())
        self.s.send(" ".encode())
        self.s.send(bytes(cla.stat_led2).encode())
        self.s.send(" ".encode())
        #self.s.send(FND[1])
        self.s.send(bytes(cla.stat_motor).encode())
        self.s.send(" ".encode())

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
