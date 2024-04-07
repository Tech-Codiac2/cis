def vernam_encrypt(plain_text, key):
    if len(plain_text) != len(key):
        raise ValueError("The length of the key must be equal to the length of the plaintext.")
    encrypted_text = ''.join(chr(ord(p) ^ ord(k)) for p, k in zip(plain_text, key))
    return encrypted_text

def vernam_decrypt(encrypted_text, key):
    if len(encrypted_text) != len(key):
        raise ValueError("The length of the key must be equal to the length of the encrypted text.")
    decrypted_text = ''.join(chr(ord(e) ^ ord(k)) for e, k in zip(encrypted_text, key))
    return decrypted_text

# Example usage:
plain_text = "Vernamcip"
key = "SECRETKEY"  # The key must be exactly the same length as the plaintext
encrypted_text = vernam_encrypt(plain_text, key)
decrypted_text = vernam_decrypt(encrypted_text, key)
print("Original Text:", plain_text)
print("Encrypted Text:", encrypted_text)
print("Decrypted Text:", decrypted_text)
