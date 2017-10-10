import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

class PIR:
    def __init__(self):
        self.pir = 24
        GPIO.setup(self.pir,GPIO.IN)
        return

    def loop(self):
        cnt = 0
        while True:
            if GPIO.input(self.pir) == True:
                print(cnt)
                cnt+=1
            time.sleep(0.1)
        return cnt

"""test code"""
pir = PIR()
try:
    pir.loop()

finally:
    GPIO.cleanup()
