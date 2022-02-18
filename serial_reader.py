import serial
import time
import os
from tkinter import *
from threading import Thread


class Chipmunk:
    def __init__(self):
        self.x = ""
        self.ser = ""
        self.main_window = Tk()
        self.main_window.title("Chipmunk")
        self.e_hex = Entry(self.main_window)
        self.e_hex.pack()
        self.e_dec = Entry(self.main_window)
        self.e_dec.pack()
        Thread(target=self.run).start()
        self.main_window.mainloop()

    def run(self):
        self.ser = serial.Serial(
            port='COM4',
            baudrate=9600,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            timeout=0)

        data = ""
        while True:
            count = 1
            for c in self.ser.read():
                count = count + 1
                if c:
                    self.x += chr(c)
                    self.e_dec.delete(0, END)
                    self.e_hex.delete(0, END)

            if len(self.x) == 18:
                out_hex = str(hex(int(self.x[1:-3]))).upper()[2:]
                out_dec = str(int(self.x[1:-3])).upper()
                self.e_hex.insert(0, out_hex)
                self.e_hex.update()
                self.e_dec.insert(0, out_dec)
                self.e_dec.update()
                self.main_window.clipboard_clear()
                self.main_window.clipboard_append(out_hex)
                self.main_window.update()
                self.x = ""
            time.sleep(0.01)
        self.ser.close()


x = Chipmunk()


