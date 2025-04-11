#editedby-> Kunj Bhardwaj
#editedon-> 7th April 2025, 02:57
#filename-> array_operations.py
#Operation on Arrays

import array
from statistics import mean, median

def array_ops(data):
    arr = array.array('i', data)
    return {
        'array': arr.tolist(),
        'length': len(arr),
        'mean': mean(arr),
        'median': median(arr),
        'max': max(arr),
        'min': min(arr),
        'sum': sum(arr),
        'sorted': sorted(arr),
        'reversed': arr[::-1],
        'squares': [x**2 for x in arr]
    }

# Example usage:
print(array_ops([1, 3, 5, 7, 9]))
