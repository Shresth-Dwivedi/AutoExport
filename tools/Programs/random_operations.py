#editedby-> Shresth Dwivedi
#editedon-> 7th April 2025, 02:41
#filename-> random_operations.py
#Operation on Random Numbers

import random
from statistics import mean, median, stdev

def random_operations(count, low, high):
    numbers = [random.randint(low, high) for _ in range(count)]
    evens = [x for x in numbers if x % 2 == 0]
    odds = [x for x in numbers if x % 2 != 0]
    return {
        'numbers': numbers,
        'count': count,
        'mean': mean(numbers),
        'median': median(numbers),
        'std_dev': stdev(numbers) if len(numbers) > 1 else 0,
        'max': max(numbers),
        'min': min(numbers),
        'sorted': sorted(numbers),
        'evens': evens,
        'odds': odds
    }

# Example usage:
print(random_operations(10, 1, 100))
