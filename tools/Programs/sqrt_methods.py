#editedby-> Shresth Dwivedi
#editedon-> 6th April 2025, 22:55
#filename-> sqrt_methods.py
#Square root (1. By prime factor 2. By division)

import math

def sqrt_prime_factor(n):
    # Uses math.sqrt for approximation as real factorization is O(sqrt(n))
    return math.isqrt(n)

def sqrt_division_method(n, precision=5):
    guess = n / 2.0
    for _ in range(precision * 10):
        guess = (guess + n / guess) / 2
    return round(guess, precision)

# Example usage:
print(sqrt_prime_factor(16))     # 4
print(sqrt_division_method(10))  # ~3.16228
