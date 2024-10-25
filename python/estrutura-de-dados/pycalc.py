# Calculator using tkinter! W/ simple GUI.
# https://www.geeksforgeeks.org/python-simple-gui-calculator-using-tkinter/

from tkinter import *

# Declare the "expression" variable globally
expression = ""

def press(num):
    # pointer to a global vars, search later
    # with it, the updated local value can be
    # used globally!
    global expression

    expression = expression + str(num)

    equation.set(expression)

def equalpress():
    try:
        global expression

        total = str(eval(expression))

        equation.set(total)

        expression = ""
    except:
        equation.set("error")
        expression = ""

def clear():
    global expression
    expression = ""
    equation.set("")

if __name__ == "__main__":

    gui = Tk()

    gui.configure(background="black")
    
    gui.title("PyCalc")

    gui.geometry("270x150")

    equation = StringVar()

    expression_field = Entry(gui, textvariable=equation)
