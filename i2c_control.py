import smbus2 as smbus
import time

class I2C:
    def __init__(self):
        self.bus = smbus.SMBus(1)
        self.addr = 0
        self.reset_val = 0
        return

    def read_byte(self,write_val):
        self.bus.write_byte(self.addr,write_val)
        time.sleep(0.260)
        data1 = self.bus.read_byte(self.addr)
        data2 = self.bus.read_byte(self.addr)
        return (data1<<8)|data2

    def reset(self):
        self.bus.write_byte(self.addr,self.reset_val)
        return

class I2C_light(I2C):
    def __init__(self):
        super().__init__()
        self.addr = 0x23
        self.reset_val = 0x07
        self.con_hr_mode = 0x10

    def check_light(self):
        val = self.read_byte(self.con_hr_mode)
        return val/1.2

class I2C_temp_humi(I2C):
    def __init__(self):
        super().__init__()
        self.addr = 0x40
        self.reset_val = 0xfe
        self.temp = 0xf3
        self.humi = 0xf5

    def check_temp(self):
        val = self.read_byte(self.temp)
        return -46.85+175.72/65536*val

    def check_humi(self):
        val = self.read_byte(self.humi)
        return -6.0+125.0/65536*val

class FND(I2C):
    def __init__(self):
        super().__init__()
        self.addr = 0x20
        self.config_port = 0x06
        self.output_port = 0x02
        self.data = (0xFC,0x60,0xDA,0xF2,0x66,0xB6,0x3E,0xE0,0xFE,0xF6,0xEE,0xF8,0x72,0xBC,0xF2,0xE2)
        self.digit = (0x7F,0xBF,0xDF,0xEF,0xF7,0xFB)
        self.out_disp = 0
        self.bus.write_word_data(self.addr,self.config_port,0x0000) #?
        return

    def display_data(self,data,digit = 0):
        out_disp = self.data[data]<<8|self.digit[digit]
        self.bus.write_word_data(self.addr,self.output_port,out_disp)
        return

    def reset(self):
        for i in range(6):
            out_disp = 0x00<<8|self.digit[i]
            self.bus.write_word_data(self.addr,self.output_port,out_disp)
        return

"""Test code"""
# light = I2C_light()
# temp_humi = I2C_temp_humi()
# fnd = FND()
# try:
#     while True:
#         for i in range(6):
#             for j in range(10):
#                 fnd.display_data(j,i)
#                 time.sleep(0.1)
#         print("light: {:0.2f}".format(light.check_light()))
#         print("temp: {:0.2f}".format(temp_humi.check_temp()))
#         print("humi: {:0.2f}".format(temp_humi.check_humi()))
# finally:
#     fnd.reset()
