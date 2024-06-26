def diffie_hellman(prime, generator, private_key):
    """Diffie-Hellman key exchange."""
    public_key = pow(generator, private_key, prime)
    return public_key

def generate_shared_secret(prime, public_key, private_key):
    """Generate shared secret using the received public key."""
    shared_secret = pow(public_key, private_key, prime)
    return shared_secret

# Example usage:
prime = 23  # A prime number, often denoted as p
generator = 5  # A primitive root modulo p
alice_private_key = 6
bob_private_key = 15
# Alice computes her public key
alice_public_key = diffie_hellman(prime, generator, alice_private_key)
# Bob computes his public key
bob_public_key = diffie_hellman(prime, generator, bob_private_key)
# The shared secret is generated by both Alice and Bob
alice_shared_secret = generate_shared_secret(prime, bob_public_key, alice_private_key)
bob_shared_secret = generate_shared_secret(prime, alice_public_key, bob_private_key)
# Both Alice and Bob now have the same shared secret
print("Shared Secret (Alice):", alice_shared_secret)
print("Shared Secret (Bob):", bob_shared_secret)
