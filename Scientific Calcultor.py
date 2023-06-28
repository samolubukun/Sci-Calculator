from tkinter import *
import math

def click_number(number):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(END, current + str(number))

def click_operator(operator):
    entry.insert(END, operator)

def calculate():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, END)
        entry.insert(END, result)
    except Exception as e:
        entry.delete(0, END)
        entry.insert(END, "Error")

def calculate_square_root():
    try:
        number = float(entry.get())
        result = math.sqrt(number)
        entry.delete(0, END)
        entry.insert(END, result)
    except Exception as e:
        entry.delete(0, END)
        entry.insert(END, "Error")

def calculate_power():
    try:
        expression = entry.get()
        parts = expression.split("^")
        if len(parts) != 2:
            raise ValueError("Invalid input")
        base = float(parts[0])
        exponent = float(parts[1])
        result = base ** exponent
        entry.delete(0, END)
        entry.insert(END, result)
    except Exception as e:
        entry.delete(0, END)
        entry.insert(END, "Error")

def calculate_sin():
    try:
        angle = float(entry.get())
        result = math.sin(math.radians(angle))
        entry.delete(0, END)
        entry.insert(END, result)
    except Exception as e:
        entry.delete(0, END)
        entry.insert(END, "Error")

def calculate_cos():
    try:
        angle = float(entry.get())
        result = math.cos(math.radians(angle))
        entry.delete(0, END)
        entry.insert(END, result)
    except Exception as e:
        entry.delete(0, END)
        entry.insert(END, "Error")

def calculate_tan():
    try:
        angle = float(entry.get())
        result = math.tan(math.radians(angle))
        entry.delete(0, END)
        entry.insert(END, result)
    except Exception as e:
        entry.delete(0, END)
        entry.insert(END, "Error")

def calculate_log():
    try:
        number = float(entry.get())
        result = math.log10(number)
        entry.delete(0, END)
        entry.insert(END, result)
    except Exception as e:
        entry.delete(0, END)
        entry.insert(END, "Error")

def calculate_factorial():
    try:
        number = int(entry.get())
        result = math.factorial(number)
        entry.delete(0, END)
        entry.insert(END, result)
    except Exception as e:
        entry.delete(0, END)
        entry.insert(END, "Error")

# Create the main window
master = Tk()
master.title("Scientific Calculator")

# Create the entry field
entry = Entry(master)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Create the number buttons
button_1 = Button(master, text="1", padx=10, pady=5, command=lambda: click_number(1))
button_1.grid(row=1, column=0)

button_2 = Button(master, text="2", padx=10, pady=5, command=lambda: click_number(2))
button_2.grid(row=1, column=1)

button_3 = Button(master, text="3", padx=10, pady=5, command=lambda: click_number(3))
button_3.grid(row=1, column=2)

button_4 = Button(master, text="4", padx=10, pady=5, command=lambda: click_number(4))
button_4.grid(row=2, column=0)

button_5 = Button(master, text="5", padx=10, pady=5, command=lambda: click_number(5))
button_5.grid(row=2, column=1)

button_6 = Button(master, text="6", padx=10, pady=5, command=lambda: click_number(6))
button_6.grid(row=2, column=2)

button_7 = Button(master, text="7", padx=10, pady=5, command=lambda: click_number(7))
button_7.grid(row=3, column=0)

button_8 = Button(master, text="8", padx=10, pady=5, command=lambda: click_number(8))
button_8.grid(row=3, column=1)

button_9 = Button(master, text="9", padx=10, pady=5, command=lambda: click_number(9))
button_9.grid(row=3, column=2)

button_0 = Button(master, text="0", padx=10, pady=5, command=lambda: click_number(0))
button_0.grid(row=4, column=1)

# Create the operator buttons
button_plus = Button(master, text="+", padx=10, pady=5, command=lambda: click_operator("+"))
button_plus.grid(row=1, column=3)

button_minus = Button(master, text="-", padx=10, pady=5, command=lambda: click_operator("-"))
button_minus.grid(row=2, column=3)

button_multiply = Button(master, text="*", padx=10, pady=5, command=lambda: click_operator("*"))
button_multiply.grid(row=3, column=3)

button_divide = Button(master, text="/", padx=10, pady=5, command=lambda: click_operator("/"))
button_divide.grid(row=4, column=3)

# Create the calculate button
button_equals = Button(master, text="=", padx=10, pady=5, command=calculate)
button_equals.grid(row=4, column=2)

# Create the clear button
button_clear = Button(master, text="Clear", padx=10, pady=5, command=lambda: entry.delete(0, END))
button_clear.grid(row=4, column=0)

# Create the square root button
button_sqrt = Button(master, text="√", padx=10, pady=5, command=calculate_square_root)
button_sqrt.grid(row=5, column=0)

# Create the power button
button_power = Button(master, text="^", padx=10, pady=5, command=calculate_power)
button_power.grid(row=5, column=1)

# Create the trigonometric buttons
button_sin = Button(master, text="sin", padx=10, pady=5, command=calculate_sin)
button_sin.grid(row=5, column=2)

button_cos = Button(master, text="cos", padx=10, pady=5, command=calculate_cos)
button_cos.grid(row=5, column=3)

# Create the logarithm button
button_log = Button(master, text="log", padx=10, pady=5, command=calculate_log)
button_log.grid(row=6, column=0)

# Create the factorial button
button_fact = Button(master, text="!", padx=10, pady=5, command=calculate_factorial)
button_fact.grid(row=6, column=1)

# Create the tangent button
button_tan = Button(master, text="tan", padx=10, pady=5, command=calculate_tan)
button_tan.grid(row=6, column=2)

# Start the main loop
master.mainloop()
