#editedby-> Shresth Dwivedi
#editedon-> 5th April 2025, 13:01
#filename-> armstrong_check.py
#Find if the Given Number is Armstrong or Not

def is_armstrong(n):
    digits = str(n)
    power = len(digits)
    return n == sum(int(d)**power for d in digits)

# Example usage:
print(is_armstrong(153))  # True
print(is_armstrong(123))  # False
