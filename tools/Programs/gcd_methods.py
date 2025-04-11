#editedby-> Kunj Bhardwaj
#editedon-> 7th April 2025, 00:31
#filename-> gcd_methods.py
#GCD (1. Prime factor 2. Long division 3. List of factors)

def gcd_prime_factors(a, b):
    def factors(n):
        result = set()
        d = 2
        while d * d <= n:
            if n % d == 0:
                result.add(d)
                n //= d
            else:
                d += 1
        if n > 1:
            result.add(n)
        return result

    return max(factors(a).intersection(factors(b)), default=1)

def gcd_long_division(a, b):
    while b:
        a, b = b, a % b
    return a

def gcd_list_factors(a, b):
    def all_factors(n):
        return {i for i in range(1, n + 1) if n % i == 0}
    return max(all_factors(a).intersection(all_factors(b)))

# Example usage:
print(gcd_prime_factors(12, 18))   # 3
print(gcd_long_division(12, 18))   # 6
print(gcd_list_factors(12, 18))    # 6
