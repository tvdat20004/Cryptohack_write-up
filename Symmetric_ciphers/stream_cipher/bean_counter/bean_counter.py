from requests import Session
from pwn import xor
import json
s = Session()
url = 'https://aes.cryptohack.org/bean_counter/'
def encrypt():
	data = s.get(url + 'encrypt/').text
	ct = json.loads(data)['encrypted']
	return bytes.fromhex(ct)


enc = encrypt()
png_header = b'\x89\x50\x4E\x47\x0D\x0A\x1A\x0A\x00\x00\x00\x0D\x49\x48\x44\x52'
# ctr_enc = xor(png_header, enc[16:])
ctr_enc = bytes([a^b for a,b in zip(png_header, enc[:16])])
decrypted = b''

blocks = [enc[i:i+16] for i in range(0,len(enc),16)]
for block in blocks:
	decrypted += bytes([a^b for a,b in zip(block, ctr_enc)])
	# decrypted += xor(block, ctr_enc)

with open('flag.png', 'wb') as out:
	out.write(decrypted)
