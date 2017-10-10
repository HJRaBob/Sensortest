##raspberrypi all the class

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

class LED:
    def __init__(self):
        GPIO.setup(14,GPIO.OUT)
        GPIO.setup(15,GPIO.OUT)
        self.leds = [14, 15]
        self.leds[0] = GPIO.PWM(14,100)
        self.leds[1] = GPIO.PWM(15,100)
        return


    def led_on(self,ldnum, duty = 100):
        self.leds[ldnum].start(duty)

        return

    def led_off(self,ldnum):
        self.leds[ldnum].stop()

        return

class PIEZO:
    def __init__(self):
        piezo_pin=13
        GPIO.setup(13,GPIO.OUT)
        self.scale = [261,294,329,349,392,440,493,523,587,659,698,783]
        self.sound = GPIO.PWM(13,100)
        self.flag = 0

        return

    def make_scale(self):
        self.sound.start(100)

        for i in range(8):
            self.sound.ChangeFrequency(self.scale[i])
            time.sleep(0.5)
        return

    def piezo_off(self):
        self.sound.ChangeDutyCycle(0)
        self.sound.stop()
        return

class MOTOR:
    def __init__(self):
        GPIO.setup(4,GPIO.OUT)
        GPIO.setup(25,GPIO.OUT)
        GPIO.setup(12,GPIO.OUT)
        self.motors=[4,25,12]   #RP,RN,EN

        self.motors[2] = GPIO.PWM(self.GPIO_EN,100)
        self.motors[2].start(0)
        return


    def cw(self,duty = 100):
        GPIO.output(self.motors[0],True)
        GPIO.output(self.motors[1],False)
        GPIO.output(self.motors[2],True)
        self.EN.ChangeDutyCycle(duty)
        return

    def ccw(self,duty = 100):
        GPIO.output(self.motors[0],False)
        GPIO.output(self.motors[1],True)
        GPIO.output(self.motors[2],True)
        self.EN.ChangeDutyCycle(duty)
        return

    def motor_change_speed(p,duty):
        p.ChangeDutyCycle(duty)

    def motor_off(self):
        GPIO.output.stop(self.motors[2],False)

        return

class LCD:

    def __init__(self):

        self.LCD_RS = 23
        self.LCD_E  = 26
        self.LCD_D4 = 17
        self.LCD_D5 = 18
        self.LCD_D6 = 27
        self.LCD_D7 = 22
        self.LCD_WIDTH = 16    # Maximum characters per line
        self.LCD_CHR = True; self.LCD_CMD = False
        self.LCD_LINE_1 = 0x80; self.LCD_LINE_2 = 0xC0
        self.E_PULSE = 0.0005; self.E_DELAY = 0.0005

        GPIO.setup(self.LCD_E, GPIO.OUT)  # E
        GPIO.setup(self.LCD_RS, GPIO.OUT) # RS
        GPIO.setup(self.LCD_D4, GPIO.OUT) # DB4
        GPIO.setup(self.LCD_D5, GPIO.OUT) # DB5
        GPIO.setup(self.LCD_D6, GPIO.OUT) # DB6
        GPIO.setup(self.LCD_D7, GPIO.OUT) # DB7

        return self.reset()


    def reset(self):
        self.lcd_byte(0x33,self.LCD_CMD) # 110011 Initialise
        self.lcd_byte(0x32,self.LCD_CMD) # 110010 Initialise
        self.lcd_byte(0x06,self.LCD_CMD) # 000110 Cursor move direction
        self.lcd_byte(0x0C,self.LCD_CMD) # 001100 Display On,Cursor Off, Blink Off
        self.lcd_byte(0x28,self.LCD_CMD) # 101000 Data length, number of lines, font size
        self.lcd_byte(0x01,self.LCD_CMD) # 000001 Clear display
        time.sleep(self.E_DELAY)
        return

    def lcd_byte(self, bits, mode):
        GPIO.output(self.LCD_RS, mode)
        GPIO.output(self.LCD_D4, False)
        GPIO.output(self.LCD_D5, False)
        GPIO.output(self.LCD_D6, False)
        GPIO.output(self.LCD_D7, False)
        if bits&0x10==0x10:
            GPIO.output(self.LCD_D4, True)
        if bits&0x20==0x20:
            GPIO.output(self.LCD_D5, True)
        if bits&0x40==0x40:
            GPIO.output(self.LCD_D6, True)
        if bits&0x80==0x80:
            GPIO.output(self.LCD_D7, True)
        self.lcd_toggle_enable()

        GPIO.output(self.LCD_D4, False)
        GPIO.output(self.LCD_D5, False)
        GPIO.output(self.LCD_D6, False)
        GPIO.output(self.LCD_D7, False)
        if bits&0x01==0x01:
            GPIO.output(self.LCD_D4, True)
        if bits&0x02==0x02:
            GPIO.output(self.LCD_D5, True)
        if bits&0x04==0x04:
            GPIO.output(self.LCD_D6, True)
        if bits&0x08==0x08:
            GPIO.output(self.LCD_D7, True)
        self.lcd_toggle_enable()
        return

    def lcd_toggle_enable(self):
        time.sleep(self.E_DELAY)
        GPIO.output(self.LCD_E, True)
        time.sleep(self.E_PULSE)
        GPIO.output(self.LCD_E, False)
        time.sleep(self.E_DELAY)
        return

    def lcd_string(self,message,line=1):
        message = message.ljust(self.LCD_WIDTH," ")
        if line == 1:
            self.lcd_byte(self.LCD_LINE_1, self.LCD_CMD)
        elif line == 2:
            self.lcd_byte(self.LCD_LINE_2, self.LCD_CMD)
        else:
            print('line must be 1 or 2')
        for i in range(self.LCD_WIDTH):
            self.lcd_byte(ord(message[i]),self.LCD_CHR)
        return

    def lcd_clear(self):
        return self.lcd_byte(0x01,self.LCD_CMD)

    def lcd_home(self):
        return self.lcd_byte(0x02,self.LCD_CMD)

    def lcd_cursor_shift(self,direction,many):
        if direction == 0:
            for i in range(many):
                self.lcd_byte(0x10,self.LCD_CMD)
        elif direction == 1:
            for i in range(many):
                self.lcd_byte(0x14,self.LCD_CMD)
        else:
            print ('direction must be 0 or 1')
        return

    def lcd_screen_shift(self,direction,many):
        if direction == 0:
            for i in range(many):
                self.lcd_byte(0x18,self.LCD_CMD)
        elif direction == 1:
            for i in range(many):
                self.lcd_byte(0x1C,self.LCD_CMD)
        else:
            print ('direction must be 0 or 1')
        return

class JoyStick:
    def __init__(self):
        self.pin = [5,6,16,20,21] #up down left right cen
        self.stat = [0,0,0,0,0]
        for i in self.pin:
            GPIO.setup(i,GPIO.IN)
        return

    def read_stat(self):
        for i in range(len(self.pin)):
            self.cur_stat = GPIO.input(self.pin[i])
            if self.cur_stat != self.stat[i]:
                self.stat[i] = self.cur_stat
                if self.cur_stat == 1:
                    return i

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

class UltraSonic:
    def __init__(self):
        self.trig = 0
        self.echo = 1

        GPIO.setup(self.trig,GPIO.OUT)
        GPIO.setup(self.echo,GPIO.IN)

        return

    def sonic_check(self):
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


#test
if __name__ == "__main__":
    lcd = LCD()
    sonic = UltraSonic()
    joy = JoyStick()
    led = LED()
    piezo = PIEZO()


    try:
        while 1:
            #lcd test
            lcd.lcd_string("Distance:{0}cm".format(sonic.sonic_check()),1)

    finally:
        GPIO.cleanup()
