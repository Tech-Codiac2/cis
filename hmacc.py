import hmac
import hashlib

def generate_hmac(message, key, hash_function=hashlib.sha256):
    """Generate an HMAC signature."""
    hmac_signature = hmac.new(key.encode('utf-8'), message.encode('utf-8'), hash_function)
    return hmac_signature.digest()

def verify_hmac(message, key, received_signature, hash_function=hashlib.sha256):
    """Verify an HMAC signature."""
    expected_signature = generate_hmac(message, key, hash_function)
    return hmac.compare_digest(expected_signature, received_signature)

# Example usage:
secret_key = "my_secret_key"
message_to_sign = "Hello, HMAC!"

# Generating an HMAC signature
signature = generate_hmac(message_to_sign, secret_key)
print("Generated HMAC Signature:", signature)

# Verifying the HMAC signature
is_valid = verify_hmac(message_to_sign, secret_key, signature)
print("Signature Verification Result:", is_valid)
