#editedby-> Shresth Dwivedi
#editedon-> 3rd April 2025, 09:44
#filename-> area_calculations.py
#Area of the Triangle, Rectangle, Square, Circle

import math

def area_triangle(base, height):
    return 0.5 * base * height

def area_rectangle(length, width):
    return length * width

def area_square(side):
    return side * side

def area_circle(radius):
    return math.pi * radius ** 2

# Example usage:
print(area_triangle(3, 4))    # 6.0
print(area_rectangle(5, 4))   # 20
print(area_square(4))         # 16
print(area_circle(3))         # ~28.27
