#editedby-> Kunj Bhardwaj
#editedon-> 6th April 2025, 13:45
#filename-> swap_values.py
#Swapping values 1. temporary 2. Without temporary

def swap_temp(a, b):
    temp = a
    a = b
    b = temp
    return a, b

def swap_no_temp(a, b):
    a, b = b, a
    return a, b

# Example usage:
print(swap_temp(3, 4))     # (4, 3)
print(swap_no_temp(10, 20)) # (20, 10)
