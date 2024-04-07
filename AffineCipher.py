def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

def encrypt(plain_text, a, b, m):
    cipher_text = ''
    for char in plain_text:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            encrypted_char = chr(((ord(char) - ord('a')) * a + b) % m + ord('a'))
            cipher_text += encrypted_char.upper() if is_upper else encrypted_char
        else:
            cipher_text += char
    return cipher_text

def decrypt(cipher_text, a, b, m):
    a_inv = mod_inverse(a, m)
    plain_text = ''
    for char in cipher_text:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            decrypted_char = chr((a_inv * (ord(char) - ord('a') - b)) % m + ord('a'))
            plain_text += decrypted_char.upper() if is_upper else decrypted_char
        else:
            plain_text += char
    return plain_text

# Example usage:
plain_text = "Hello, Affine Cipher!"
a, b, m = 3, 5, 26
cipher_text = encrypt(plain_text, a, b, m)
decrypted_text = decrypt(cipher_text, a, b, m)
print("Original Text:", plain_text)
print("Encrypted Text:", cipher_text)
print("Decrypted Text:", decrypted_text)
