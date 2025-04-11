#editedby-> Kunj Bhardwaj
#editedon-> 6th April 2025, 18:10
#filename-> reverse_values.py
#Reverse integer and string

def reverse_string(s):
    return s[::-1]

def reverse_integer(n):
    sign = -1 if n < 0 else 1
    return sign * int(str(abs(n))[::-1])

# Example usage:
print(reverse_string("hello"))  # "olleh"
print(reverse_integer(1234))    # 4321
