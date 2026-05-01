import secrets
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes

def aes_ed(message):
    key = secrets.token_bytes(32)
    nonce = secrets.token_bytes(12)

    aes = AESGCM(key)

    ciphertext = nonce + aes.encrypt(nonce,message.encode(),None)
    plainText = aes.decrypt(ciphertext[:12], ciphertext[12:],None)

    return key.hex() , ciphertext.hex(), plainText.decode()

if __name__ == "__main__":
    print(aes_ed("Hello, AES!"))
