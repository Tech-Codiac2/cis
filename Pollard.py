import math

def pollards_p_minus_1(n, max_steps=1000):
    """Pollard's P-1 factorization algorithm."""
    a = 2  # Initial value for the random element

    for j in range(2, max_steps + 1):
        a = pow(a, j, n)  # Compute a^j mod n

        d = math.gcd(a - 1, n)
        if 1 < d < n:
            return d  # Found a non-trivial factor
        elif d == n:
            return None  # n itself is prime, no non-trivial factors
    return None  # No non-trivial factors found within the specified limit

# Example usage:
composite_number = 221
factor = pollards_p_minus_1(composite_number)

if factor:
    other_factor = composite_number // factor
    print(f"Factors of {composite_number}: {factor} and {other_factor}")
else:
    print(f"{composite_number} may be a prime number or requires more steps.")
