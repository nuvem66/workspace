from tkinter import *

def button_press(num):
    pass

def equals():
    pass

def clear():
    pass

window = Tk()
window.title("PyCalc")
window.geometry("500x500")

equation_text = ""

equation_label = StringVar()

label = label(widow, textvariable=equation_label, text=('consolas', 20), bg="black", width=24, height=2)
label.pack()

window.mainloop()