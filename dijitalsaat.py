import tkinter as tk
import time

form=tk.Tk()
form.title("DIJITAL SAAT UYGULAMASI")
form.geometry('400x200+300+300')
form.config(bg="pink")
def zaman():
    zaman_format=time.strftime("%H:%M:%S")
    zam_label.config(text=zaman_format)
    zam_label.after(200,zaman)

zam_label=tk.Label(bg="white",font="time 14")
zam_label.place(x=160,y=80)
zaman()

form.mainloop()
