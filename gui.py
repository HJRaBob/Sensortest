from tkinter import *
from tkinter import ttk
import GUIclass as mylib
import time

class GUI:

    def __init__(self):
        win = Tk()
        win.title('2 GUI')

        #Input
        self.joy=mylib.JoyStick()
        self.pir=mylib.PIR()
        #self.light=mylib.Light()
        self.us=mylib.UltraSonic()
        self.temp=mylib.Temp_humi()

        #Output
        self.lcd=mylib.LCD()
        self.led=mylib.LED()
        self.piezo=mylib.Piezo()
        #self.fnd=mylib.FND()
        #self.motor=mylib.MOTOR()

        self.text1 = ttk.Label(win, text=" INPUT ")
        self.text1.grid(column=0, row=0)
        #self.text1.config(font = (18, 'bold'))


        self.i1 = ttk.Label(win, text=" JOY stick ")
        self.i1.grid(column=0, row=1)
        self.i2 = ttk.Label(win, text=" PIR ")
        self.i2.grid(column=0, row=2)
        self.i3 = ttk.Label(win, text=" 조도 ")
        self.i3.grid(column=0, row=3)
        self.i4 = ttk.Label(win, text=" UltraSonic ")
        self.i4.grid(column=0, row=4)
        self.i5 = ttk.Label(win, text=" Temp/Humi ")
        self.i5.grid(column=0, row=5)
        self.i6 = ttk.Label(win, text=" Light ")
        self.i6.grid(column=0, row=6)

        self.in1 = ttk.Label(win, text="                ")
        self.in1.grid(column=1, row=1)
        self.in2 = ttk.Label(win, text="                ")
        self.in2.grid(column=1, row=2)
        self.in3 = ttk.Label(win, text="                ")
        self.in3.grid(column=1, row=3)
        self.in4 = ttk.Label(win, text="                ")
        self.in4.grid(column=1, row=4)
        self.in5 = ttk.Label(win, text="                ")
        self.in5.grid(column=1, row=5)
        self.in6 = ttk.Label(win, text="                ")
        self.in6.grid(column=1, row=6)


        self.emp1 = ttk.Label(win, text="------------------------")
        self.emp1.grid(column=0, row=6)
        self.emp2 = ttk.Label(win, text="------------------------")
        self.emp2.grid(column=1, row=6)

        self.text2 = ttk.Label(win, text=" OUTPUT ")
        self.text2.grid(column=0, row=7)
        #self.text2.config(font = (18, 'bold'))


        self.ot1 = ttk.Label(win, text=" LCD ")
        self.ot1.grid(column=0, row=8)
        self.ot2 = ttk.Label(win, text=" LED ")
        self.ot2.grid(column=0, row=9)
        self.ot3 = ttk.Label(win, text=" PIEZO ")
        self.ot3.grid(column=0, row=10)
        self.ot4 = ttk.Label(win, text=" FND ")
        self.ot4.grid(column=0, row=11)
        self.ot5 = ttk.Label(win, text=" MOTOR ")
        self.ot5.grid(column=0, row=12)

        self.out1 = ttk.Label(win, text="                ")
        self.out1.grid(column=1, row=8)
        self.out2 = ttk.Label(win, text="                ")
        self.out2.grid(column=1, row=9)
        self.out3 = ttk.Label(win, text="                ")
        self.out3.grid(column=1, row=10)
        self.out4 = ttk.Label(win, text="                ")
        self.out4.grid(column=1, row=11)
        self.out5 = ttk.Label(win, text="                ")
        self.out5.grid(column=1, row=12)

        self.checkcheck()
        win.mainloop()

        return


    def checkcheck(self):
        print("checkcheck")
        self.check_stat_joy()
        self.check_stat_led()
        self.check_stat_ultrasonic()
        self.check_stat_temp()
        #self.check_stat_motor()
        time.sleep(1)


    def check_stat_joy(self):
        print("joy")
        if self.joy.read_stat() == 0:
            self.in1.config(text=" UP ")
        elif self.joy.read_stat() == 1:
            self.in1.config(text=" DOWN ")
        elif self.joy.read_stat() == 2:
            self.in1.config(text=" LEFT ")
        elif self.joy.read_stat() == 3:
            self.in1.config(text=" RIGHT ")
        elif self.joy.read_stat() == 4:
            self.in1.config(text=" CENTER ")
        else :
            self.in1.config(text=" NOT WORKING ")



    def check_stat_led(self):
        print("led")
        if self.led.stat_led[0] == 1 and self.led.stat_led[1] == 1 :
            self.out2.config(text=" ALL LED ON")

        elif self.led.stat_led[0] == 1 and self.led.stat_led[1] == 0 :
            self.out2.config(text=" FIRST LED ON")

        elif self.led.stat_led[0] == 0 and self.led.stat_led[1] == 1 :
            self.out2.config(text=" SECOND LED ON")

        elif self.led.stat_led[0] == 0 and self.led.stat_led[1] == 0 :
            self.out2.config(text=" ALL LED OFF")

    def check_stat_ultrasonic(self):
        print("ultrasonic")
        self.in4.config(text = self.us.sonic_check())

    def check_stat_temp(self):
        print("Temp_humi")
        self.in5.config(text = str(self.temp.check_temp()) + " / " +  str(self.temp.check_humi()) )



    # def check_stat_piezo(self):
    #     #if piezo의 상태
    #     #piezzo 가 켜지면 self.out3.config(text=" PIEZO ON")
    #     #piezo 가 꺼지면 self.out3.config(text=" PIEZO OFF")


    # def check_stat_fnd(self):
    #     #if fnd의 상태
    #     #piezzo 가 켜지면 self.out4.config(text=" FND ON")
    #     #led 가 꺼지면 self.out4.config(text=" FND OFF")
    #

    # def check_stat_motor(self):
    #     if self.motor.stat_motor == 0:
    #         self.out5.config(text=" STOP ")
    #     elif self.motor.stat_motor == 1:
    #         self.out5.config(text="CW ")
    #     elif self.motor.stat_motor == 2:
    #         self.out5.config(text=" CCW ")

if __name__ == "__main__":

    gui = GUI()
