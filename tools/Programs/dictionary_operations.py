#editedby-> Shresth Dwivedi
#editedon-> 7th April 2025, 02:11
#filename-> dictionary_operations.py
#Operation on Dictionary

def dict_ops(d):
    return {
        'keys': list(d.keys()),
        'values': list(d.values()),
        'items': list(d.items()),
        'sorted_by_key': dict(sorted(d.items()))
    }

# Example usage:
print(dict_ops({'b': 2, 'a': 1, 'c': 3}))
