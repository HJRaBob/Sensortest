from tkinter import *
from tkinter import ttk
import GUIclass as mylib

class GUI:

    def __init__(self):
        win = Tk()
        win.title('2 GUI')
        self.us=mylib.UltraSonic()

        self.text = ttk.Label(win, text=" 거리가 10cm 이상이면 불이 켜집니다.")
        self.text.grid(column=1, row=0)
        self.text1 = ttk.Label(win, text=" 거리가 나타납니다")
        self.text1.grid(column=1, row=1)

        self.btn_stat=0

        self.btn1 = ttk.Button(win,text="측정 시작",command=self.btn_on)
        self.btn1.grid(column=0,row=2)
        self.btn2 = ttk.Button(win,text="측정 종료",command=self.btn_off)
        self.btn2.grid(column=2,row=2)
        win.mainloop()
        return


    def btn_on(self):
        self.btn_stat=1
        self.btn_onoff()

    def btn_off(self):
        self.btn_stat=0
        self.text1.config(text="중지되었습니다.")

    def btn_onoff(self):
        self.text1.config(text="Distance:{0}cm".format(self.us.sonic_check()))
        self.led_onoff()



    def stat_on_text(self):
        self.text.config(text=" 불이 켜졌습니다.")

    def stat_off_text(self):
        self.text.config(text=" 불이 꺼졌습니다.")

    def led_onoff(self):
        if self.us.sonic_check() > 10 :
            self.stat_on_text()
        else :
            self.stat_off_text()



if __name__ == "__main__":

    gui = GUI()
