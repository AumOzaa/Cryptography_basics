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

def verify_intergrity(file1,file2):
    hash1 = hash_file(file1)
    hash2 = hash_file(file2)

    print(f"Checking integrity between {file1} and {file2}")

    if hash1 == hash2:
        return "File is intact (AI giving 2 blue ticks :)"
    return "File has been modified"

if __name__ == "__main__":
    print(f"SHA hash of this file is : {hash_file("sample_files/sample.txt")}")
    print(verify_intergrity("sample_files/sample.txt","sample_files/sample.txt"))
