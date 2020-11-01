from tkinter import *

root = Tk()
root.title("Calculator")

entryBox = Entry(root, width = 35, borderwidth = 5)
entryBox.grid(row = 0, column = 0, columnspan = 3, padx = 10, pady = 10)

def button_click(buttonCommand):
    current = entryBox.get()
    entryBox.delete(0, END)
    entryBox.insert(0, str(current) + str(buttonCommand))

def clear_function():
    entryBox.delete(0, END)

def add_function():
    first_num = entryBox.get()
    global f_num
    global math
    math = "add"
    f_num = int(first_num)
    entryBox.delete(0, END)

def equal_function():
    if (entryBox.get() != ""):
        global f_num
        second_number = int(entryBox.get())
        entryBox.delete(0, END)
        if math == "add":
            entryBox.insert(0, f_num + second_number)
        elif math == "sub":
            entryBox.insert(0, f_num - second_number)
        elif math == "mult":
            entryBox.insert(0, f_num * second_number)
        elif math == "div":
            entryBox.insert(0, f_num / second_number)

        f_num = 0

def sub_function():
    first_num = entryBox.get()
    global f_num
    global math
    math = "sub"
    f_num = int(first_num)
    entryBox.delete(0, END)

def mult_function():
    first_num = entryBox.get()
    global f_num
    global math
    math = "mult"
    f_num = int(first_num)
    entryBox.delete(0, END)

def div_function():
    first_num = entryBox.get()
    global f_num
    global math
    math = "div"
    f_num = int(first_num)
    entryBox.delete(0, END)



button1 = Button(root, text = "1", padx = 40, pady = 20, command = lambda : button_click(1))
button2 = Button(root, text = "2", padx = 40, pady = 20, command = lambda : button_click(2))
button3 = Button(root, text = "3", padx = 40, pady = 20, command = lambda : button_click(3))
button4 = Button(root, text = "4", padx = 40, pady = 20, command = lambda : button_click(4))
button5 = Button(root, text = "5", padx = 40, pady = 20, command = lambda : button_click(5))
button6 = Button(root, text = "6", padx = 40, pady = 20, command = lambda : button_click(6))
button7 = Button(root, text = "7", padx = 40, pady = 20, command = lambda : button_click(7))
button8 = Button(root, text = "8", padx = 40, pady = 20, command = lambda : button_click(8))
button9 = Button(root, text = "9", padx = 40, pady = 20, command = lambda : button_click(9))
button0 = Button(root, text = "0", padx = 40, pady = 20, command = lambda : button_click(0))

button_add = Button(root, text = "+", padx = 39, pady = 20, command = add_function)
button_sub = Button(root, text = "-", padx = 40, pady = 20, command = sub_function)
button_mult = Button(root, text = "*", padx = 41, pady = 20, command = mult_function)
button_div = Button(root, text = "/", padx = 40, pady = 20, command = div_function)
button_equal = Button(root, text = "=", padx = 91, pady = 20, command = equal_function)
button_clear = Button(root, text = "AC", padx = 85, pady = 20, command = clear_function)

# grid system of the buttons
button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)
button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)
button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)
button0.grid(row=4, column=0)

button_add.grid(row = 5, column = 0)
button_equal.grid(row = 5, column = 1, columnspan = 2)
button_clear.grid(row = 4, column = 1, columnspan = 2)

button_sub.grid(row = 6, column = 0)
button_mult.grid(row = 6, column = 1)
button_div.grid(row = 6, column = 2)



root.mainloop()