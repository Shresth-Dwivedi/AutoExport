#editedby-> Kunj Bhardwaj
#editedon-> 7th April 2025, 02:46
#filename-> list_operations.py
#Operation on List

def list_ops(lst):
    return {
        'original': lst,
        'length': len(lst),
        'sorted': sorted(lst),
        'reversed': lst[::-1],
        'unique': list(set(lst)),
        'sum': sum(lst),
        'mean': sum(lst) / len(lst) if lst else 0,
        'max': max(lst),
        'min': min(lst),
        'frequency': {x: lst.count(x) for x in set(lst)}
    }

# Example usage:
print(list_ops([5, 2, 3, 2, 8, 5]))
