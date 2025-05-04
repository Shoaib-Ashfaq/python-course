import sys
import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b

def sqrt(a):
    if a < 0:
        raise ValueError("Cannot take square root of a negative number.")
    return math.sqrt(a)

try:
    if len(sys.argv) < 3:
        raise ValueError("Not enough arguments. Usage: python cli_calculator.py <operation> <number1> [number2]")

    operation = sys.argv[1].lower()
    num1 = float(sys.argv[2])

    if operation in ["add", "subtract", "multiply", "divide"]:
        if len(sys.argv) < 4:
            raise ValueError("Two numbers required for this operation.")
        num2 = float(sys.argv[3])

    if operation == "add":
        result = add(num1, num2)
    elif operation == "subtract":
        result = subtract(num1, num2)
    elif operation == "multiply":
        result = multiply(num1, num2)
    elif operation == "divide":
        result = divide(num1, num2)
    elif operation == "sqrt":
        result = sqrt(num1)
    else:
        raise ValueError("Unsupported operation.")

    print(f"Result: {result}")

except ValueError as ve:
    print(f"Value Error: {ve}")
except ZeroDivisionError as zde:
    print(f"Math Error: {zde}")
except Exception as e:
    print(f"Unexpected Error: {e}")

