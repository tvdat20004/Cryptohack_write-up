from requests import Session
import json
s = Session()
def get_encrypt(pt : bytes):
	url = "https://aes.cryptohack.org/ecb_oracle/encrypt/"
	url += pt.hex()
	response = json.loads(s.get(url).text)
	ct = response["ciphertext"]
	return bytes.fromhex(ct)

def find_flag(encrypt, flag_format,length_flag):
	flag = flag_format
	while b'}' not in flag:
		l = len(flag)
		send = b'a'*(length_flag - l - 1)
		sample_ct = encrypt(send)[:length_flag]
		for c in range(33,127):
			# print(c)
			send = b'a'*(length_flag-l-1) + flag + c.to_bytes()
			ct = encrypt(send)[:length_flag]
			if ct == sample_ct:
				flag += c.to_bytes()
				print(flag)
				break
flag = b'crypto{'
find_flag(get_encrypt, flag, 32)
# crypto{p3n6u1n5_h473_3cb}	
