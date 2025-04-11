#editedby-> Kunj Bhardwaj
#editedon-> 6th April 2025, 20:05
#filename-> base_conversion.py
#Base conversion

def to_binary(n):
    return bin(n)[2:]

def to_octal(n):
    return oct(n)[2:]

def to_hexadecimal(n):
    return hex(n)[2:]

# Example usage:
print(to_binary(10))       # "1010"
print(to_octal(10))        # "12"
print(to_hexadecimal(255)) # "ff"
