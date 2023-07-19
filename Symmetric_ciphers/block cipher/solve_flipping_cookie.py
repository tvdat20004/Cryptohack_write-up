from requests import Session
import os
import json

s = Session()

def get_cookie():
	url = "https://aes.cryptohack.org/flipping_cookie/get_cookie/"
	data = json.loads(s.get(url).text) 
	ct = data["cookie"]
	return bytes.fromhex(ct)

def check_admin(cookie, iv):
	url = "https://aes.cryptohack.org/flipping_cookie/check_admin/" + cookie.hex() + '/' + iv.hex() + '/'
	data = json.loads(s.get(url).text)
	try:
		flag = data["flag"]
		return flag
	except:
		return data


def flipping_bits(ciphertext, pos, plaintext : bytes, new_plaintext : bytes):
	assert len(plaintext) == len(new_plaintext)
	ciphertext = list(ciphertext)
	for i in range(pos, pos + len(plaintext)):
		ciphertext[i] = ciphertext[i] ^ (plaintext[i-pos] ^ new_plaintext[i-pos])
	iv = ciphertext[:16]
	ct = ciphertext[16:]
	return bytes(iv),bytes(ct)



ciphertext = get_cookie()

iv, ct = flipping_bits(ciphertext, 6, b'False', b'True;')

print(check_admin(ct, iv))
# crypto{4u7h3n71c4710n_15_3553n714l}