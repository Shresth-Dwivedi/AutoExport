#editedby-> Kunj Bhardwaj
#editedon-> 6th April 2025, 10:46
#filename-> prime_check.py
#Find Given Number is Prime or Not

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

# Example usage:
print(is_prime(7))    # True
print(is_prime(12))   # False
