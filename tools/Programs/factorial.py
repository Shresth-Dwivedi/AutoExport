#editedby-> Kunj Bhardwaj
#editedon-> 6th April 2025, 17:42
#filename-> factorial.py
#Factorial (simple and recursive)

def factorial_iter(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def factorial_rec(n):
    if n == 0:
        return 1
    return n * factorial_rec(n - 1)

# Example usage:
print(factorial_iter(5))  # 120
print(factorial_rec(5))   # 120
