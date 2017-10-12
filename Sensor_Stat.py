import GUIclass as mylib
import time

class Libraury:

    def __init__(self):

        #Input
        self.joy=mylib.JoyStick()
        self.pir=mylib.PIR()
        self.light=mylib.Light()
        self.us=mylib.UltraSonic()
        self.temp=mylib.Temp_humi()

        #Output
        self.lcd=mylib.LCD()
        self.led=mylib.LED()
        self.piezo=mylib.Piezo()
        self.fnd=mylib.FND()
        self.motor=mylib.MOTOR()

        self.stat_joy = 5
        self.stat_pir = 0
        self.stat_light = 0
        self.stat_led1 = 0
        self.stat_led2 = 0
        self.tat_ultrasonic = 0
        self.stat_temp = 0
        self.stat_humi = 0
        self.stat_piezo = 0
        self.stat_motor = 0

        self.check_stat()



    def check_stat(self):

        self.stat_joy = self.joy.read_stat
        self.stat_pir = self.pir.loop()
        self.stat_light = self.light.light_check()
        self.stat_led1 = GPIO.input(14)
        self.stat_led2 = GPIO.input(15)
        self.stat_ultrasonic = self.us.sonic_check()
        self.stat_temp = self.temp.check_temp()
        self.stat_humi = self.temp.check_humi()
        self.stat_piezo = GPIO.input(13)
        self.stat_motor = self.motor.motor_stat()
