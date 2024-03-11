def add(a,b):
    return a + b

def sub(a,b):
    return a -b

def multiply(a,b):
    return a * b

def div(a, b):
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return a / b
