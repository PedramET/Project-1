# Calculator

import math
import tkinter as tk



def power_function(x,y):
    return math.pow(x,y)

def sin_function(x):
    return math.sin(math.radians(x))

def cos_function(x):
    return math.cos(math.radians(x))

def tan_function(x):
    return math.tan(math.radians(x))

def cot_function(x):
    return 1 / math.tan(math.radians(x))

def sqrt_function(x):
    return math.sqrt(x)

def log_function(x):
    return math.log(x)

def e_function(x):
    return math.e


def operation(operation):
    if operation == "^": return power_function
    elif operation == "sin": return sin_function
    elif operation == "cos": return cos_function
    elif operation == "tan": return tan_function
    elif operation == "cot": return cot_function
    elif operation == "sqrt": return sqrt_function
    elif operation == "log": return log_function
    elif operation == "e": return e_function
    else: return ("Unknown Operation")


def evaluate(expression):
    try:
        result = eval(expression)
        return result
    except Exception as e:
        return f"Error: {e}"
    
def display_window():
    window = tk.Tk()
    window.title("Calculator")
    window.geometry("400x400")
    #...
