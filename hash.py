import hashlib

text = "password123"

hash_object = hashlib.sha256(text.encode())
hash_digest = hash_object.hexdigest()

print(f"Real password {text} and the hashed password {hash_digest}")


def hash_file(file_path):
    h = hashlib.new("sha256")
    with open(file_path, "rb") as file:
        while True:
            chunk = file.read(1024) # 1024 bytes
            if chunk == b"":
                break
            h.update(chunk)

        return h.hexdigest()

if __name__ == "__main__":
    print(f"SHA hash of this file is : {hash_file("sample_files/sample.txt")}")
