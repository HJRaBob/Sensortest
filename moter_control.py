import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

class Motor:
    def __init__(self):
        self.GPIO_RP = 4
        self.GPIO_RN = 25
        self.GPIO_EN = 12
        GPIO.setup(self.GPIO_RP,GPIO.OUT)
        GPIO.setup(self.GPIO_RN,GPIO.OUT)
        GPIO.setup(self.GPIO_EN,GPIO.OUT)
        self.EN = GPIO.PWM(self.GPIO_EN,100)
        self.EN.start(0)
        return

    def cw(self,duty = 100):
        GPIO.output(self.GPIO_RP,True)
        GPIO.output(self.GPIO_RN,False)
        GPIO.output(self.GPIO_EN,True)
        self.EN.ChangeDutyCycle(duty)
        return

    def ccw(self,duty = 100):
        GPIO.output(self.GPIO_RP,False)
        GPIO.output(self.GPIO_RN,True)
        GPIO.output(self.GPIO_EN,True)
        self.EN.ChangeDutyCycle(duty)
        return

    def chang_speed(self,duty):
        self.EN.ChangeDutyCycle(duty)

    def stop(self):
        GPIO.output(self.GPIO_EN,False)
        return


"""#Test"""
# motor = Motor()
# try:
#     while True:
#         print 'forword'
#         motor.cw()
#         time.sleep(1)
#
#         print 'stop'
#         motor.stop()
#         time.sleep(1)
#
#         print('backword')
#         motor.ccw(50)
#         time.sleep(1)
#
#         print('stop')
#         motor.stop()
#         time.sleep(1)
# finally:
#     print("Cleaning up")
#     GPIO.cleanup()
