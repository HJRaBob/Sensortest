from tkinter import *
from tkinter import ttk
import Sensor_Stat as s_s
import time

class GUI:

    def __init__(self):

        self.win = Tk()
        self.win.title('CLIENT')


        self.text1 = ttk.Label(self.win, text=" INPUT ")
        self.text1.grid(column=0, row=0)
        #self.text1.config(font = ('bold')


        self.i1 = ttk.Label(self.win, text=" JOY stick ")
        self.i1.grid(column=0, row=1)
        self.i2 = ttk.Label(self.win, text=" PIR ")
        self.i2.grid(column=0, row=2)
        self.i3 = ttk.Label(self.win, text=" Light ")
        self.i3.grid(column=0, row=3)
        self.i4 = ttk.Label(self.win, text=" UltraSonic ")
        self.i4.grid(column=0, row=4)
        self.i5 = ttk.Label(self.win, text=" Temp/Humi ")
        self.i5.grid(column=0, row=5)


        self.in1 = ttk.Label(self.win, text="                ")
        self.in1.grid(column=1, row=1)
        self.in2 = ttk.Label(self.win, text="                ")
        self.in2.grid(column=1, row=2)
        self.in3 = ttk.Label(self.win, text="                ")
        self.in3.grid(column=1, row=3)
        self.in4 = ttk.Label(self.win, text="                ")
        self.in4.grid(column=1, row=4)
        self.in5 = ttk.Label(self.win, text="                ")
        self.in5.grid(column=1, row=5)


        self.emp1 = ttk.Label(self.win, text="-----------------------------")
        self.emp1.grid(column=0, row=6)
        self.emp2 = ttk.Label(self.win, text="-----------------------------")
        self.emp2.grid(column=1, row=6)

        self.text2 = ttk.Label(self.win, text=" OUTPUT ")
        self.text2.grid(column=0, row=7)
        #self.text2.config(font = ( 'bold')


        self.ot1 = ttk.Label(self.win, text=" LCD ")
        self.ot1.grid(column=0, row=8)
        self.ot2 = ttk.Label(self.win, text=" LED ")
        self.ot2.grid(column=0, row=9)
        self.ot3 = ttk.Label(self.win, text=" PIEZO ")
        self.ot3.grid(column=0, row=10)
        self.ot4 = ttk.Label(self.win, text=" FND ")
        self.ot4.grid(column=0, row=11)
        self.ot5 = ttk.Label(self.win, text=" MOTOR ")
        self.ot5.grid(column=0, row=12)

        self.out1 = ttk.Label(self.win, text="                ")
        self.out1.grid(column=1, row=8)
        self.out2 = ttk.Label(self.win, text="                ")
        self.out2.grid(column=1, row=9)
        self.out3 = ttk.Label(self.win, text="                ")
        self.out3.grid(column=1, row=10)
        self.out4 = ttk.Label(self.win, text="                ")
        self.out4.grid(column=1, row=11)
        self.out5 = ttk.Label(self.win, text="                ")
        self.out5.grid(column=1, row=12)

        self.checkcheck()

        return


    def checkcheck(self):

        print("checkcheck")

        self.ss=s_s.Libraury()
        self.check_stat_joy()
        self.check_stat_pir()
        self.check_stat_light()
        self.check_stat_led()
        self.check_stat_ultrasonic()
        self.check_stat_temp()
        self.check_stat_piezo()
        self.check_stat_motor()

        self.win.update()



    def check_stat_joy(self):
        print("joy")
        if self.ss.stat_joy == 0:
            self.in1.config(text=" UP ")
        elif self.ss.stat_joy == 1:
            self.in1.config(text=" DOWN ")
        elif self.ss.stat_joy == 2:
            self.in1.config(text=" LEFT ")
        elif self.ss.stat_joy == 3:
            self.in1.config(text=" RIGHT ")
        elif self.ss.stat_joy == 4:
            self.in1.config(text=" CENTER ")
        else :
            self.in1.config(text=" NOT WORKING ")

    def check_stat_pir(self):
        print("pir")
        self.in2.config(text= self.ss.stat_pir)

    def check_stat_light(self):
        print("light")
        self.in3.config(text= self.ss.stat_light)

    def check_stat_led(self):
        print("led")
        if self.ss.stat_led1 == 1 and self.ss.stat_led2 == 1 :
            self.out2.config(text=" ALL LED ON")

        elif self.ss.stat_led1 == 1 and self.ss.stat_led2 == 0 :
            self.out2.config(text=" FIRST LED ON")

        elif self.ss.stat_led1 == 0 and self.ss.stat_led2 == 1 :
            self.out2.config(text=" SECOND LED ON")

        elif self.ss.stat_led1 == 0 and self.ss.stat_led2 == 0 :
            self.out2.config(text=" ALL LED OFF")

    def check_stat_ultrasonic(self):
        print("ultrasonic")
        self.in4.config(text = self.ss.stat_ultrasonic)

    def check_stat_temp(self):
        print("Temp_humi")
        self.in5.config(text = str(self.ss.stat_temp) + " / " +  str(self.ss.stat_humi) )


    def check_stat_piezo(self):
        if self.ss.stat_piezo == 1:
            self.out3.config(text=" ON ")

        else :
            self.out3.config(text=" OFF ")

    # def check_stat_fnd(self):
    #     #if fnd의 상태
    #     #fnd 가 켜지면 self.out4.config(text=" FND ON")
    #     #fnd 가 꺼지면 self.out4.config(text=" FND OFF")
    #


    def check_stat_motor(self):
        if self.ss.stat_motor == 0:
            self.out5.config(text=" STOP ")
        elif self.ss.stat_motor == 1:
            self.out5.config(text="CW ")
        elif self.ss.stat_motor == 2:
            self.out5.config(text=" CCW ")



if __name__ == "__main__":
    gui = GUI()
    while True:
        gui.checkcheck()
