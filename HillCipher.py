import numpy as np

# Function to generate the key matrix from the key string
def generate_key_matrix(key):
    n = int(np.sqrt(len(key)))
    key_matrix = np.array([ord(char) - ord('A') for char in key]).reshape(n, n)
    return key_matrix

# Function to encrypt plaintext using Hill cipher
def encrypt_hill(plain_text, key):
    n = int(np.sqrt(len(key)))
    key_matrix = generate_key_matrix(key)
    
    # Pad the plain text with 'X' if its length is not a multiple of n
    if len(plain_text) % n != 0:
        plain_text += 'X' * (n - len(plain_text) % n)
    
    # Convert the plain text to numerical values
    plain_text_num = np.array([ord(char) - ord('A') for char in plain_text])
    plain_text_matrix = plain_text_num.reshape(-1, n)
    
    # Encrypt each block of the plain text
    encrypted_matrix = (np.dot(plain_text_matrix, key_matrix) % 26).flatten()
    
    # Convert the numerical encrypted text back to characters
    encrypted_text = ''.join([chr(val + ord('A')) for val in encrypted_matrix])
    
    return encrypted_text

# Function to decrypt cipher text using Hill cipher
def decrypt_hill(cipher_text, key):
    n = int(np.sqrt(len(key)))
    key_matrix = generate_key_matrix(key)
    
    # Calculate the determinant of the key matrix
    determinant = np.linalg.det(key_matrix)
    key_matrix_inv = None
    
    # Check if the determinant is invertible
    if np.gcd(int(determinant), 26) == 1:
        # Calculate the modular inverse of the determinant
        determinant_inv = pow(int(determinant), -1, 26)
        
        # Calculate the adjugate of the key matrix
        adjugate_matrix = determinant * np.linalg.inv(key_matrix)
        
        # Calculate the inverse of the key matrix
        key_matrix_inv = (determinant_inv * adjugate_matrix) % 26
    
    # If the key matrix is not invertible, return None
    if key_matrix_inv is None:
        return None
    
    # Convert the cipher text to numerical values
    cipher_text_num = np.array([ord(char) - ord('A') for char in cipher_text])
    cipher_text_matrix = cipher_text_num.reshape(-1, n)
    
    # Decrypt each block of the cipher text
    decrypted_matrix = (np.dot(cipher_text_matrix, key_matrix_inv) % 26).flatten()
    
    # Convert the numerical decrypted text back to characters
    decrypted_text = ''.join([chr(int(val) + ord('A')) for val in decrypted_matrix])
    
    return decrypted_text

# Example usage:
plain_text = "HELLO"
key = "GYBNQKURP"
cipher_text = encrypt_hill(plain_text, key)
decrypted_text = decrypt_hill(cipher_text, key)

print("Original Text:", plain_text)
print("Encrypted Text:", cipher_text)
print("Decrypted Text:", plain_text)
