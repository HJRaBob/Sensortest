import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

class Jog:
    def __init__(self):
        self.pin = [5,6,16,20,21]
        for i in self.pin:
            GPIO.setup(i,GPIO.IN)
        return

    def read_stat(self,func):
        #func is function tuple (up,down,left,right,cen)
        for i in range(len(self.pin)):
            cur_stat = GPIO.input(self.pin[i])
            if cur_stat == 1:
                return func[i]()


"""Test Class"""
# class Motor:
#     def __init__(self):
#         self.GPIO_RP = 4
#         self.GPIO_RN = 25
#         self.GPIO_EN = 12
#         GPIO.setup(self.GPIO_RP,GPIO.OUT)
#         GPIO.setup(self.GPIO_RN,GPIO.OUT)
#         GPIO.setup(self.GPIO_EN,GPIO.OUT)
#         self.EN = GPIO.PWM(self.GPIO_EN,100)
#         self.EN.start(0)
#         return
#
#     def cw(self,duty):
#         GPIO.output(self.GPIO_RP,True)
#         GPIO.output(self.GPIO_RN,False)
#         GPIO.output(self.GPIO_EN,True)
#         self.EN.ChangeDutyCycle(duty)
#         return
#
#     def ccw(self,duty):
#         GPIO.output(self.GPIO_RP,False)
#         GPIO.output(self.GPIO_RN,True)
#         GPIO.output(self.GPIO_EN,True)
#         self.EN.ChangeDutyCycle(duty)
#         return
#
#     def change_speed(self,duty):
#         self.EN.ChangeDutyCycle(duty)
#         return
#
#     def stop(self):
#         GPIO.output(self.GPIO_RP,False)
#         GPIO.output(self.GPIO_RN,False)
#         GPIO.output(self.GPIO_EN,False)
#         return


# class Control_motor:
#     def __init__(self):
#         self.motor = Motor()
#         self.jog = Jog()
#         self.speed = 50
#         self.control = \
#         (self.when_up,self.when_down,self.when_left,self.when_right,self.when_cen)
#
#     def when_up(self):
#         self.speed += 10
#         return self.motor.change_speed(self.speed)
#
#     def when_down(self):
#         self.speed -= 10
#         return self.motor.change_speed(self.speed)
#
#     def when_left(self):
#         return self.motor.cw(self.speed)
#
#     def when_right(self):
#         return self.motor.ccw(self.speed)
#
#     def when_cen(self):
#         return self.motor.stop()
#
#     def check_mode(self):
#         return self.jog.read_stat(self.control)
#
#
# c = Control_motor()
# try:
#     while True:
#         c.check_mode()
#         time.sleep(1)
# except BaseException:
#     print(c.speed)
# finally:
#     GPIO.cleanup()
