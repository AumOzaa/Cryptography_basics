# AES-GCM Encryption - Questions & Answers

## Q1: Is the key generated per request?

**In this demo: YES** - both the key and nonce are generated fresh every time the function runs.

**In real applications: NO** - the key would be:
- Generated **once** and stored securely (database, key vault, environment variable)
- Reused for many encryptions
- Only the **nonce** changes per encryption

```python
# Real-world pattern:
MASTER_KEY = os.getenv("ENCRYPTION_KEY")  # Stored once, reused

def encrypt_message(message):
    nonce = secrets.token_bytes(12)  # New nonce each time
    aes = AESGCM(MASTER_KEY)
    ...
```

---

## Q2: What is a cipher?

A **cipher** is the algorithm that transforms plaintext ↔ ciphertext.

```
Plaintext ("Hello") + Key + Nonce
           ↓
      [AES-GCM Cipher Algorithm]
           ↓
Ciphertext (gibberish bytes)
```

Think of it like:
- **Key** = the specific combination for a lock
- **Cipher (AES-GCM)** = the lock mechanism design itself

---

## Q3: Is this AES key the same as a JWT signing key?

**Similar concept, different purpose:**

| Aspect | AES-GCM Key (this code) | JWT Signing Key |
|--------|------------------------|-----------------|
| Purpose | **Encryption** - hides the message content | **Signing** - proves authenticity, doesn't hide content |
| Secret? | Yes - must be kept secret | Yes - must be kept secret |
| What it does | Transforms data so only key-holders can read | Creates a signature to detect tampering |
| Data visibility | Content is encrypted (hidden) | JWT payload is **visible** (base64, not encrypted) |

### JWT Verification Flow:
```
JWT = header.payload.signature

signature = HMAC_SHA256(header.payload, secret_key)

# Verification:
1. Recreate signature from header.payload + your copy of secret_key
2. Compare with the signature in the JWT
3. If they match → not tampered
```

### AES-GCM Flow:
```
1. Encrypt: message + key + nonce → ciphertext
2. Decrypt: ciphertext + key + nonce → message
3. If tampered → decryption FAILS (GCM detects it)
```

**Key similarity:** Both use a secret key to detect tampering.

**Key difference:**
- **JWT** = signs visible data (anyone can read payload)
- **AES-GCM** = encrypts hidden data + includes authentication tag
