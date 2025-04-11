#editedby-> Kunj Bhardwaj
#editedon-> 2nd April 2025, 21:13
#filename-> simple_calculator.py
#Simple Calculator

def calculator(a, b, operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        return a / b if b != 0 else "Division by zero"
    elif operator == '%':
        return a % b if b != 0 else "Modulo by zero"
    else:
        return "Invalid operator"

# Example usage:
print(calculator(10, 5, '+'))  # 15
