# Calculator


import math

math_operation = {
    "^":    math.pow,
    "sqrt": math.sqrt,
    "sin":  math.sin,
    "cos":  math.cos,
    "tan":  math.tan,
}

def evaluate(input):
    try:
        result = eval(input, math_operation)
        return result
    except Exception as e:
        return f"Error: {e}"
    

