def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, x, y = extended_gcd(b % a, a)
        return g, y - (b // a) * x, x

def mod_inverse(a, m):
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise Exception("The modular inverse does not exist")
    else:
        return x % m

def chinese_remainder_theorem(congruences):
    # Compute M, the product of all moduli
    M = 1
    for _, m in congruences:
        M *= m
    
    result = 0
    for a, m in congruences:
        # Compute Mi and xi
        Mi = M // m
        xi = mod_inverse(Mi, m)
        # Calculate the contribution of each congruence
        result += a * Mi * xi
    
    return result % M

# Example usage:
congruences = [(2, 3), (3, 5), (2, 7)]
result = chinese_remainder_theorem(congruences)
print("The solution is:", result)
