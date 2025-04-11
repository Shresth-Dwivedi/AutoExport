#editedby-> Kunj Bhardwaj
#editedon-> 6th April 2025, 13:12
#filename-> fibonacci_series.py
#Print Fibonacci Series

def fibonacci(n):
    a, b = 0, 1
    result = []
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result

# Example usage:
print(fibonacci(10))  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
