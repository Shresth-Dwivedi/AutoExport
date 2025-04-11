#editedby-> Kunj Bhardwaj
#editedon-> 5th April 2025, 10:59
#filename-> sum_of_digits.py
#Sum of the digits – ex. Input - 456, Output - 15

def sum_of_digits(n):
    return sum(int(d) for d in str(abs(n)))

# Example usage:
print(sum_of_digits(456))  # 15
