import hashlib

def md5_hash(message):
    """Compute the MD5 hash of a message."""
    md5 = hashlib.md5()
    md5.update(message.encode('utf-8'))
    return md5.hexdigest()

# Example usage:
message = "Hello, MD5!"
md5_digest = md5_hash(message)

print("Original Message:", message)
print("MD5 Digest:", md5_digest)
