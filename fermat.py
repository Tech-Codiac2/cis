def power_mod(base, exponent, modulus):
    result = 1
    base = base % modulus
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        exponent //= 2
        base = (base * base) % modulus
    return result

def fermat_little_theorem(a, p):
    if not (1 < a < p):
        raise ValueError("a must be an integer between 1 and p-1")
    
    result = power_mod(a, p - 1, p)
    return result == 1

# Example usage:
p = 7
a = 3
result = fermat_little_theorem(a, p)
print(f"For a = {a} and p = {p}, a^(p-1) is congruent to 1 mod p:", result)
