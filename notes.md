## Why hash a file?
### Integrity check : 
- Has the file been changed?
- Detect tampering
- Used before signing
- De-duplication

## How `hash_file()` works

```python
def hash_file(file_path):
    h = hashlib.new("sha256")
    with open(file_path, "rb") as file:
        while True:
            chunk = file.read(1024)
            if chunk == b"":
                break
            h.update(chunk)
    return h.hexdigest()
```

### Key concepts

**Chunked reading (1024 bytes)** - Reads file in small pieces instead of loading entirely into memory. Allows hashing gigabyte-sized files without running out of RAM.

**Binary mode (`"rb"`)** - Files read as raw bytes because hashing works on binary data, not text.

**`h.update(chunk)` - The internal state model:**
- `h` holds an **internal state** (256 bits for SHA-256) that starts at fixed initial values
- Each `update()` call **modifies this same state** by mixing new chunk data with the current state
- It's a "running hash" - the state accumulates all data piece by piece
- Not "hashing the previous hash" - instead, each chunk combines with the current internal state
- **Order matters**: `update(A)` then `update(B)` produces different hash than `update(B)` then `update(A)`

**`hexdigest()`** - Converts the final internal state to a 64-character hexadecimal string
