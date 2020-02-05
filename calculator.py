from tkinter import *
from tkinter import messagebox
import math

# defining the root or master window
root = Tk()
root.title('Calculator')

# commmand stack to keep track of the operators and operands
commandstack = [0, 0]

# function for inputs


def Input(n):
    """
    Gets and places the user input on to the screen
    """
    current = inputbox.get()
    inputbox.delete(0, END)
    inputbox.insert(0, current + str(n))


def addition():
    """
    Addition of the inputs provided

    Also keeps track of the operator entered and operands entered
    """
    commandstack[0] = float(inputbox.get())
    inputbox.delete(0, END)
    commandstack[1] = '+'


def subtraction():
    """
    Suubtraction of the inputs provided

    Also keeps track of the operator entered and operands entered
    """
    commandstack[0] = float(inputbox.get())
    inputbox.delete(0, END)
    commandstack[1] = '-'


def multiplication():
    """
    Multiplication of the inputs provided

    Also keeps track of the operator entered and operands entered
    """
    commandstack[0] = float(inputbox.get())
    inputbox.delete(0, END)
    commandstack[1] = '*'


def division():
    """
    Division of the inputs provided

    Also keeps track of the operator entered and operands entered
    """
    commandstack[0] = float(inputbox.get())
    inputbox.delete(0, END)
    commandstack[1] = '/'


def clear():
    """
    Clears the stack and the results after user hits clear button
    """
    inputbox.delete(0, END)
    commandstack = [0, 0]


def results():
    """
    Display results for user.
    """
    secondNumber = float(inputbox.get())
    print(commandstack)
    inputbox.delete(0, END)
    print(commandstack[0], " ", secondNumber)

    result = 0
    if commandstack[1] == '+':
        result = float(commandstack[0]) + secondNumber

    if commandstack[1] == '-':
        result = float(commandstack[0]) - secondNumber

    if commandstack[1] == '*':
        result = float(commandstack[0]) * secondNumber

    if commandstack[1] == '/':
        result = float(commandstack[0]) / secondNumber

    print(result)
    inputbox.insert(0, result)


# defining the input box on the screen for user to enter inputs.
inputbox = Entry(root, width=40, borderwidth=5)

# buttons for the calulator
button1 = Button(root, text='1', padx=45,
                 pady=15, command=lambda: Input(1))
button2 = Button(root, text='2', padx=45, pady=15, command=lambda: Input(2))
button3 = Button(root, text='3', padx=45, pady=15, command=lambda: Input(3))

button4 = Button(root, text='4', padx=45, pady=20, command=lambda: Input(4))
button5 = Button(root, text='5', padx=45, pady=20, command=lambda: Input(5))
button6 = Button(root, text='6', padx=45, pady=20, command=lambda: Input(6))

button7 = Button(root, text='7', padx=45, pady=20, command=lambda: Input(7))
button8 = Button(root, text='8', padx=45, pady=20, command=lambda: Input(8))
button9 = Button(root, text='9', padx=45, pady=20, command=lambda: Input(9))

button0 = Button(root, text='0', padx=45, pady=20, command=lambda: Input(0))
buttonClear = Button(root, text='Clear', padx=87, pady=20, command=clear)

buttonAdd = Button(root, text='+', padx=45, pady=20,
                   command=addition)
buttonEquals = Button(root, text='=', padx=97, pady=20, command=results)

buttonSub = Button(root, text='-', padx=45, pady=20,
                   command=subtraction)
buttonMult = Button(root, text='*', padx=45, pady=20,
                    command=multiplication)
buttonDiv = Button(root, text='/', padx=45, pady=20,
                   command=division)


# packing all of the buttons and the inputs on to the screen grid.
inputbox.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)

button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)

button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)

button0.grid(row=4, column=0, columnspan=1)
buttonClear.grid(row=4, column=1, columnspan=2)

buttonAdd.grid(row=5, column=0, columnspan=1)
buttonEquals.grid(row=5, column=1, columnspan=2)

buttonSub.grid(row=6, column=0, columnspan=1)
buttonMult.grid(row=6, column=1, columnspan=1)
buttonDiv.grid(row=6, column=2, columnspan=1)

root.mainloop()
