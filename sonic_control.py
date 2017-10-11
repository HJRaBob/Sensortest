import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

class Sonic_sensor:
    def __init__(self):
        self.trig = 0; self.echo = 1
        GPIO.setup(self.trig,GPIO.OUT)
        GPIO.setup(self.echo,GPIO.IN)
        return

    def check_dist(self):
        GPIO.output(self.trig,False)
        time.sleep(0.5)

        GPIO.output(self.trig,True)
        time.sleep(0.00001)
        GPIO.output(self.trig,False)
        while GPIO.input(self.echo) == False:
            pulse_start = time.time()

        while GPIO.input(self.echo) == True:
            pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start
        distance = pulse_duration*17000
        distance = round(distance,2)
        return distance

"""Test code"""
# sonic = Sonic_sensor()
# try:
#     while True:
#         print(sonic.check_dist())
#
# finally:
#     GPIO.cleanup()
