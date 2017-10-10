import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

class LED:
    def __init__(self):
        GPIO.setup(14,GPIO.OUT)
        GPIO.setup(15,GPIO.OUT)
        self.led1 = GPIO.PWM(14,100)
        self.led2 = GPIO.PWM(15,100)
        return

    def led_on_1(self,duty = 100):
        self.led1.start(duty)
        return

    def led_on_2(self,duty = 100):
        self.led2.start(duty)
        return

    def led_on(self,duty = 100):
        self.led1.start(duty)
        self.led2.start(duty)
        return

    def led_off_1(self):
        self.led1.stop()
        return

    def led_off_2(self):
        self.led2.stop()
        return

    def led_off(self):
        self.led1.stop()
        self.led2.stop()
        return

    def led_blink_1(self,delay,duty = 100):
        self.led1.start(duty)
        time.sleep(delay)
        self.led1.stop()
        return

    def led_blink_2(self,delay,duty = 100):
        self.led2.start(duty)
        time.sleep(delay)
        self.led2.stop()
        return

    def led_blink(self,delay,duty = 100):
        self.led_on(0)
        self.bright_chage_1(duty)
        self.bright_chage_2(duty)
        time.sleep(delay)
        self.bright_chage_1(0)
        self.bright_chage_2(0)
        time.sleep(delay)
        return

    def led_shift(self,delay,duty = 100):
        self.led_on(0)
        self.bright_chage_1(duty)
        self.bright_chage_2(0)
        time.sleep(delay)
        self.led_on(0)
        self.bright_chage_1(0)
        self.bright_chage_2(duty)
        time.sleep(delay)
        return

    def bright_chage_1(self,duty):
        self.led1.ChangeDutyCycle(duty)
        return

    def bright_chage_2(self,duty):
        self.led2.ChangeDutyCycle(duty)
        return

    def bright_chage(self,duty):
        self.led1.ChangeDutyCycle(duty)
        self.led2.ChangeDutyCycle(duty)
        return

"""Test"""
# led1 = 14; led2 = 15
# led = LED()
# try:
#     while True:
#         led.led_on_1(30)
#         time.sleep(1)
#         led.led_on_2(30)
#         time.sleep(1)
#         led.led_off()
#         time.sleep(1)
#         led.led_on(50)
#         time.sleep(1)
#         led.led_off_2()
#         time.sleep(1)
#         led.led_off_1()
#         time.sleep(1)
#         led.led_blink(0.5)
#         led.led_blink(0.5)
#         led.led_shift(0.5)
#         led.led_blink(0.5)
#         led.led_off()
#         time.sleep(1)
#         led.led_on(10)
#         time.sleep(1)
#         led.bright_chage_1(90)
#
# finally:
#     print("Cleaning up")
#     GPIO.cleanup()
