def encrypt_columnar(plain_text, key):
    order = sorted(range(len(key)), key=lambda k: key[k])
    cipher_text = ''
    for col in order:
        for row in range(len(plain_text) // len(key) + 1):
            idx = col + row * len(key)
            if idx < len(plain_text):
                cipher_text += plain_text[idx]
    return cipher_text

def decrypt_columnar(cipher_text, key):
    order = sorted(range(len(key)), key=lambda k: key[k])
    num_cols = len(key)
    num_rows = len(cipher_text) // num_cols
    matrix = [[''] * num_cols for _ in range(num_rows)]
    idx = 0
    for col in order:
        for row in range(num_rows):
            matrix[row][col] = cipher_text[idx]
            idx += 1
    plain_text = ''.join([''.join(row) for row in matrix])
    return plain_text

# Example usage:
plain_text = "Simple Columnar Cipher Example"
key = "COLUMNAR"
cipher_text = encrypt_columnar(plain_text, key)
decrypted_text = decrypt_columnar(cipher_text, key)
print("Original Text:", plain_text)
print("Encrypted Text:", cipher_text)
print("Decrypted Text:", decrypted_text)
