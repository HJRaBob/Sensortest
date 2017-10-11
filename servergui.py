from tkinter import *
from tkinter import ttk

class GUIserver:

    def __init__(self):
        win = Tk()
        win.title('2 GUI')
        self.text2 = ttk.Label(win, text=" CONTROL ")
        self.text2.grid(column=0, row=0)

        self.ot1 = ttk.Label(win, text=" LCD ")
        self.ot1.grid(column=0, row=1)
        self.ot2 = ttk.Label(win, text=" LED ")
        self.ot2.grid(column=0, row=2)
        self.ot3 = ttk.Label(win, text=" PIEZO ")
        self.ot3.grid(column=0, row=3)
        self.ot4 = ttk.Label(win, text=" FND ")
        self.ot4.grid(column=0, row=4)
        self.ot5 = ttk.Label(win, text=" MOTOR ")
        self.ot5.grid(column=0, row=5)

        self.lcd_value = StringVar()
        self.strlcd = ttk.Entry(win,textvariable=self.lcd_value)
        self.strlcd.grid(column=1, row=1)
        self.strlcd = ttk.Button(win, text="입력")
        self.strlcd.grid(column=2, row=1)

        self.btnled1 = ttk.Button(win, text=" 1 on",command = self.led1onoff)
        self.btnled1.grid(column=1, row=2)
        self.btnled2 = ttk.Button(win, text=" 2 on",command = self.led2onoff)
        self.btnled2.grid(column=2, row=2)

        self.btnpie1 = ttk.Button(win, text=" on",command = self.piezo_on)
        self.btnpie1.grid(column=1, row=3)
        self.btnpie2 = ttk.Button(win, text=" off",command = self.piezo_off)
        self.btnpie2.grid(column=2, row=3)

        self.fnd_value = StringVar()
        self.strfnd = ttk.Entry(win,textvariable=self.fnd_value)
        self.strfnd.grid(column=1, row=4)
        self.btnfnd = ttk.Button(win, text="입력")
        self.btnfnd.grid(column=2, row=4)

        self.btnmot1 = ttk.Button(win, text=" cw ",command = self.motor_cw())
        self.btnmot1.grid(column=1, row=5)

        self.btnmot2 = ttk.Button(win, text=" ccw ",command = self.motor_ccw())
        self.btnmot2.grid(column=2, row=5)


        self.btnmot3 = ttk.Button(win, text=" stop ",command = self.motor_stop())
        self.btnmot3.grid(column=3, row=5)
        win.mainloop()

        return

    def led1onoff(self):
        self.btnled1.config(text="1 off")

    def led2onoff(self):
        self.btnled2.config(text="2 off")

    def piezo_on(self):
        pass

    def piezo_off(self):
        pass

    def motor_cw(self):
        pass

    def motor_ccw(self):
        pass

    def motor_stop(self):
        pass




if __name__ == "__main__":

    gui = GUIserver()
