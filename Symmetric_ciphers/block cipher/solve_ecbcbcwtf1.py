from requests import Session
from Crypto.Cipher import AES
from pwn import xor
import json
s = Session()

def encrypt():
	url = "https://aes.cryptohack.org/ecbcbcwtf/encrypt_flag/"
	receive = json.loads(s.get(url).text)
	ciphertext = receive["ciphertext"]
	return bytes.fromhex(ciphertext)

def decrypt(c : bytes):
	url = "https://aes.cryptohack.org/ecbcbcwtf/decrypt/"
	url += c.hex()
	receive = json.loads(s.get(url).text)
	print(receive)
	plaintext = receive["plaintext"]
	return bytes.fromhex(plaintext)


enc = encrypt()
print(len(enc))
iv = enc[:16]
block1 = enc[16:32]
block2 = enc[32:]

decrypt_block1 = xor(decrypt(block1), iv) 
decrypt_block2 = xor(decrypt(block2), block1) 
print(decrypt_block1 + decrypt_block2)
# b'crypto{3cb_5uck5_4v01d_17_!!!!!}'