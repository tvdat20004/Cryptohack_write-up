from zlib import decompress
from requests import Session
import json


s = Session()
url = 'https://aes.cryptohack.org/ctrime/'

def encrypt(pt : bytes):
	data = s.get(url + 'encrypt/' + pt.hex() + '/').text
	ct = json.loads(data)['ciphertext']
	return bytes.fromhex(ct)

ct = encrypt(b'\x00')

pt_flag = decompress(ct)
print(pt_flag)