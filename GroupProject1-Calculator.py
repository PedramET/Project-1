# Calculator

import math
import tkinter as tk




def power_function(x,y):
    return math.pow(x,y)

def sqrt_function(x):
    return math.sqrt(x)

def sin_function(x):
    return math.sin(math.radians(x))

def cos_function(x):
    return math.cos(math.radians(x))

def tan_function(x):
    return math.tan(math.radians(x))

def cot_function(x):
    return 1 / math.tan(math.radians(x))

def log_function(x):
    return math.log(x)

def e_function(x):
    return math.e


math_operations = {
    "^":    power_function,
    "sqrt": sqrt_function,
    "sin":  sin_function,
    "cos":  cos_function,
    "tan":  tan_function,
    "cot":  cot_function,
    "log":  log_function,
    "e":    e_function,
}
    

def evaluate(expression):
    try:
        result = eval(expression, math_operations)
        return result
    except Exception as e:
        return f"Error: {e}"
    
def display_window():
    window = tk.Tk()
    window.title("Calculator")
    window.geometry("370x490")
    window.configure(bg="#000000")
    window.resizable(False,False)
    
    entry_display = tk.Entry(window, width=25 ,bg="#575757" , font=("Arial", 18))
    entry_display.grid(row=0, column=0, columnspan=4, padx=20, pady=20)
    
    def add_to_expression(value):
        entry_display.insert(tk.END, value)

    def checking_expression():
        expression = entry_display.get()
        expression = expression.replace("×", "*")
        expression = expression.replace("÷", "/")
        expression = expression.replace("^", "**")
        result = evaluate(expression)
        entry_display.delete(0, tk.END)
        entry_display.insert(0, str(result))

    def display_buttons():
        buttons = [
            ("C",1,0),("(",1,1),(")",1,2),("←",1,3),
            ("",2,0),("",2,1),("",2,2),("=",2,3),
            ("7",3,0),("8",3,1),("9",3,2),("÷",3,3),
            ("4",4,0),("5",4,1),("6",4,2),("×",4,3),
            ("1",5,0),("2",5,1),("3",5,2),("-",5,3),
            ("",6,0),("0",6,1),("",6,2),("+",6,3),
        ]

        for (text,row,col) in buttons:
            if text == "C":
                operation = lambda: entry_display.delete(0, tk.END)
            elif text == "←":
                operation = lambda: entry_display.delete(len(entry_display.get()) - 1, tk.END)
            elif text == "=":
                operation = checking_expression
            else:
                operation = lambda x = text: add_to_expression(x)
            tk.Button(window,text=text, width=5, height=3,
                     bg="#464646",fg="#FFFFFF",font=("Helvetica", 11, "bold"),
                     command=operation).grid(row=row, column=col, sticky="nswe", padx=1 , pady=1)






    display_buttons()
    window.mainloop()




display_window()