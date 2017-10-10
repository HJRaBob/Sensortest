import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

class Piezo:
    def __init__(self):
        self.piezo_pin = 13
        self.scal = [261,294,329,349,392,440,493,523,587,659,698,783]
        GPIO.setup(self.piezo_pin,GPIO.OUT)
        return

    def make_sound(self,scal = 0,vol = 90):
        self.frequency = GPIO.PWM(self.piezo_pin,self.scal[scal])
        self.frequency.start(vol)
        return

    def change_scal(self,scal):
        self.frequency.ChangeFrequency(self.scal[scal])
        return

    def stop(self):
        self.frequency.stop()
        return

"""Test code"""
# try:
#     sound = Piezo()
#     sound.make_sound()
#     time.sleep(1)
#     sound.make_sound(2)
#     time.sleep(1)
#     sound.stop()
#     time.sleep(1)
#     sound.change_scal(3)
#     time.sleep(1)
#     sound.make_sound()
#     print('change_scal')
#     for i in range(10):
#         sound.change_scal(i)
#         time.sleep(0.5)
#     print('stop')
#     sound.stop()
# finally:
#     GPIO.cleanup()
