# Calculator

import math
import tkinter as tk




def power_function(x,y):   return math.pow(x,y)
def sin_function(x):       return math.sin(math.radians(x))
def cos_function(x):       return math.cos(math.radians(x))
def tan_function(x):       return math.tan(math.radians(x))
def cot_function(x):       return 1 / math.tan(math.radians(x))

math_operations = {
    "^":         power_function,
    "sqrt":      math.sqrt,
    "sin":       sin_function,
    "cos":       cos_function,
    "tan":       tan_function,
    "cot":       cot_function,
    "log":       math.log10,
    "ln":        math.log,
    "e":         math.e,
    "pi":        math.pi,
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
        test_entry = entry_display.get()
        if test_entry and test_entry[-1] in "+-×÷" and value in "+-×÷":
            entry_display.delete(len(test_entry) - 1, tk.END)
        entry_display.insert(tk.END, value)

    def checking_expression():
        expression = entry_display.get()
        replacements = {
            "×":   "*",
            "÷":   "/",
            "^":   "**",
            "√":   "sqrt(",
            "%":   "/100",
            "sin": "sin(",
            "cos": "cos(",
            "tan": "tan(",
            "cot": "cot(",
            "log": "log(",
            "ln":  "ln(",
        }
        for (old, new) in replacements.items():
            expression = expression.replace(old, new)

        if expression.count("(") > expression.count(")"):
            expression += ")"
        result = evaluate(expression)
        entry_display.delete(0, tk.END)
        entry_display.insert(0, str(result))

    def display_buttons():
        buttons = [
            ("C",1,0),("(",1,1),(")",1,2),("←",1,3),
            ("...",2,0),("%",2,1),("√",2,2),("÷",2,3),
            ("7",3,0),("8",3,1),("9",3,2),("×",3,3),
            ("4",4,0),("5",4,1),("6",4,2),("-",4,3),
            ("1",5,0),("2",5,1),("3",5,2),("+",5,3),
            ("0",6,0),(".",6,1),("^",6,2),("=",6,3),
        ]

        for (text,row,col) in buttons:
            if text == "C":
                operation = lambda: entry_display.delete(0, tk.END)
            elif text == "←":
                operation = lambda: entry_display.delete(len(entry_display.get()) - 1, tk.END)
            elif text == "=":
                operation = checking_expression
            elif text == "^":
                operation = lambda: add_to_expression("^")
            elif text == "√": 
                operation = lambda: add_to_expression("√")
            elif text == "%":
                operation = lambda: add_to_expression("%")
            elif text == "...":
                operation = extra_buttons
            else:
                operation = lambda x = text: add_to_expression(x)
            tk.Button(window,text=text, width=5, height=3,
                     bg="#464646",fg="#FFFFFF",font=("Helvetica", 11, "bold"),
                     command=operation).grid(row=row, column=col, sticky="nswe", padx=1 , pady=1)
             
    def extra_buttons():
        second_window = tk.Toplevel()
        second_window.title("Calculator")
        second_window.geometry("265x105")
        second_window.resizable(False,False)
        second_window.configure(bg="#222222")
        more_buttons = [
            ("sin",1,0),("cos",1,1),("tan",1,2),("cot",1,3),
            ("ln",2,0),("log",2,1),("e",2,2),("π",2,3),
        ]

        for (text,row,col) in more_buttons:
            if text == "sin":
                operation = lambda: add_to_expression("sin")
            elif text == "cos":
                operation = lambda: add_to_expression("cos")
            elif text == "tan":
                operation = lambda: add_to_expression("tan")
            elif text == "cot":
                operation = lambda: add_to_expression("cot")
            elif text == "ln":
                operation = lambda: add_to_expression("ln")
            elif text == "log":
                operation = lambda: add_to_expression("log")
            elif text == "e":
                operation = lambda: add_to_expression(str(math.e))
            elif text == "π":
                operation = lambda: add_to_expression(str(math.pi))

            tk.Button(second_window, text= text, width=6, height=2, 
                      bg="#464646", fg="#FFFFFF", font=("Helvetica", 11, "bold"),
                      command=operation).grid(row=row, column= col, sticky="nswe", padx=1, pady=1)

    display_buttons()
    window.mainloop()

display_window()