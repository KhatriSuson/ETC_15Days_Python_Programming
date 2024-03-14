
try:
    # Attempt to execute Python code with invalid syntax
    eval("print('Hello, World!'")
except SyntaxError as e:
    # Handle the SyntaxError
    print("Error: Invalid syntax in Python code ", e)



