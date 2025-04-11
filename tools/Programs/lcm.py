#editedby-> Kunj Bhardwaj
#editedon-> 7th April 2025, 01:12
#filename-> lcm.py
#Lowest Common Multiple

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

# Example usage:
print(lcm(12, 15))  # 60
