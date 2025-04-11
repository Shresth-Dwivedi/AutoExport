#editedby-> Kunj Bhardwaj
#editedon-> 7th April 2025, 02:49
#filename-> set_operations.py
#Operation on Sets

def set_ops(a, b):
    return {
        'set_A': a,
        'set_B': b,
        'union': a | b,
        'intersection': a & b,
        'difference_A_B': a - b,
        'difference_B_A': b - a,
        'symmetric_difference': a ^ b,
        'is_disjoint': a.isdisjoint(b),
        'is_A_subset_B': a.issubset(b),
        'is_B_subset_A': b.issubset(a)
    }

# Example usage:
print(set_ops({1, 2, 3}, {3, 4, 5}))
