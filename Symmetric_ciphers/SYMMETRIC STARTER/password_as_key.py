cipher_flag ='c92b7734070205bdf6c0087a751466ec13ae15e6f1bcdd3f3a535ec0f4bbae66'
import hashlib
from Crypto.Cipher import AES
with open("words.txt") as f:
    words = [w.strip() for w in f.readlines()]


def decrypt(ciphertext, password_hash):
    ciphertext = bytes.fromhex(ciphertext)
    key = bytes.fromhex(password_hash)

    cipher = AES.new(key, AES.MODE_ECB)
    try:
        decrypted = cipher.decrypt(ciphertext)
    except ValueError as e:
        return {"error": str(e)}
    return decrypted

for w in words:
	key = hashlib.md5(w.encode()).digest()
	flag = decrypt(cipher_flag, key.hex())
	if b'crypto' in flag:
		print(flag)

