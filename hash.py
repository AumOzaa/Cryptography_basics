import hashlib

text = "password123"

hash_object = hashlib.sha256(text.encode())
hash_digest = hash_object.hexdigest()

print(f"Real password {text} and the hashed password {hash_digest}")
