# Calculator Project

# Subtraction Function
def subtraction(a, b): 
    return a - b

# Addition Function
def add(a, b): 
    return a + b

# Division Function
def div(a, b):
    if b == 0:
        return "Error: Cannot divide by zero" 
    return a / b

# Multiplication Function
def mul(a, b):
    return a * b

# User Input with Error Handling
try:
    n = input("Enter Operator (+, -, /, *): ").strip() 
    if n not in ["+", "-", "/", "*"]:
        raise ValueError("Invalid Operator")
    a = float(input("Enter value 1: ")) 
    b = float(input("Enter value 2: "))
except ValueError as e:
    print(f"Error: {e}. Please enter valid inputs.")
else:
    # Performing Calculation
    if n == "-":
        result = subtraction(a, b)
    elif n == "+":
        result = add(a, b)
    elif n == "/":
        result = div(a, b)
    elif n == "*":
        result = mul(a, b)

    print(f"Result: {result}")
