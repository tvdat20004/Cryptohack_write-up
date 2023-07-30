from requests import Session
import json
s = Session()

url = 'https://aes.cryptohack.org/symmetry/'
def enc_flag():
	data = s.get(url + 'encrypt_flag/').text
	ct = json.loads(data)['ciphertext']
	return bytes.fromhex(ct)

def encrypt(pt: bytes, iv: bytes):
	data = s.get(url + 'encrypt/' + pt.hex() + '/' + iv.hex() + '/').text
	ct = json.loads(data)['ciphertext']
	return bytes.fromhex(ct)

ct = enc_flag()
iv = ct[:16]
pt = ct[16:]

print(encrypt(pt,iv))
# b'crypto{0fb_15_5ymm37r1c4l_!!!11!}'