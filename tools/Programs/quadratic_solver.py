#editedby-> Kunj Bhardwaj
#editedon-> 3rd April 2025, 22:35
#filename-> quadratic_solver.py
#Quadratic Equation

import math

def solve_quadratic(a, b, c):
    d = b ** 2 - 4 * a * c
    if d > 0:
        root1 = (-b + math.sqrt(d)) / (2 * a)
        root2 = (-b - math.sqrt(d)) / (2 * a)
        return "Real and Distinct", root1, root2
    elif d == 0:
        root = -b / (2 * a)
        return "Real and Equal", root
    else:
        real = -b / (2 * a)
        imag = math.sqrt(-d) / (2 * a)
        return "Complex", complex(real, imag), complex(real, -imag)

# Example usage:
print(solve_quadratic(1, -3, 2))  # (Real and Distinct, 2.0, 1.0)
