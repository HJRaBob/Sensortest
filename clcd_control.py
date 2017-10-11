import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

class CLCD:
    def __init__(self):
        self.LCD_RS = 23; self.LCD_RW = 24; self.LCD_E = 26; self.LCD_D4 = 17
        self.LCD_D5 = 18; self.LCD_D6 = 27; self.LCD_D7 = 22
        self.LCD_WIDTH = 16; self.LCD_CHR = True; self.LCD_CMD = False
        self.LCD_LINE_1 = 0x80; self.LCD_LINE_2 = 0xC0
        self.E_PULSE = 0.0005; self.E_DELAY = 0.0005
        GPIO.setup(self.LCD_E,GPIO.OUT)
        GPIO.setup(self.LCD_RS,GPIO.OUT)
        GPIO.setup(self.LCD_D4,GPIO.OUT)
        GPIO.setup(self.LCD_D5,GPIO.OUT)
        GPIO.setup(self.LCD_D6,GPIO.OUT)
        GPIO.setup(self.LCD_D7,GPIO.OUT)
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
        GPIO.output(self.LCD_RS, mode) # RS
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

    def lcd_string(self,message,line = 1):
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

"""Test code"""
# clcd = CLCD()
# clcd.lcd_cursor_shift(1,3)
# clcd.lcd_byte(ord('h'),True)
# time.sleep(5)
# clcd.lcd_string('hello')
# time.sleep(5)
# clcd.lcd_string('good')
# clcd.lcd_string('bye',2)
# time.sleep(5)
# clcd.lcd_home()
# clcd.lcd_string('look')
# time.sleep(5)
# clcd.lcd_screen_shift(1,2)
# time.sleep(5)
# clcd.lcd_string('hello')
# time.sleep(5)
# clcd.reset()
# GPIO.cleanup()
