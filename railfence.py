def encrypt_rail_fence(plain_text, num_rows):
    rail = [''] * num_rows
    direction = 1  # 1 for down, -1 for up
    row = 0
    for char in plain_text:
        rail[row] += char
        row += direction
        if row == num_rows - 1 or row == 0:
            direction *= -1
    cipher_text = ''.join(rail)
    return cipher_text

def decrypt_rail_fence(cipher_text, num_rows):
    rail = [''] * num_rows
    direction = 1
    row = 0
    for char in cipher_text:
        rail[row] += ' '
        row += direction
        if row == num_rows - 1 or row == 0:
            direction *= -1
    idx = 0
    for i in range(num_rows):
        for j in range(len(rail[i])):
            rail[i] = rail[i][:j] + cipher_text[idx] + rail[i][j + 1:]
            idx += 1
    plain_text = ''.join(rail)
    return plain_text.replace(' ', '')

# Example usage:
plain_text = "Rail Fence Cipher Example"
num_rows = 3
cipher_text = encrypt_rail_fence(plain_text, num_rows)
decrypted_text = decrypt_rail_fence(cipher_text, num_rows)
print("Original Text:", plain_text)
print("Encrypted Text:", cipher_text)
print("Decrypted Text:", decrypted_text)
