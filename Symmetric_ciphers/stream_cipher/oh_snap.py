from requests import Session
import json
from collections import Counter
from tqdm import trange
s = Session()
url = "https://aes.cryptohack.org/oh_snap/send_cmd/"
def get_encrypted(nonce, ciphertext):
	ciphertext = ciphertext.hex()
	nonce = nonce.hex()
	recv = json.loads(s.get(url + ciphertext + '/' + nonce).text)

	if "msg" in recv:
		return b'ping'
	else:
		return bytes.fromhex(recv['error'].split(':')[1])

def _possible_key_bit(key, c):
    s = [i for i in range(256)]
    j = 0
    for i in range(len(key)):
        j = (j + s[i] + key[i]) % 256
        tmp = s[i]
        s[i] = s[j]
        s[j] = tmp

    return (c[0] - j - s[len(key)]) % 256


def attack(encrypt_oracle, key_len):
    """
    Recovers the hidden part of an RC4 key using the Fluhrer-Mantin-Shamir attack.
    :param encrypt_oracle: the padding oracle, returns the encryption of a plaintext under a hidden key concatenated with the iv
    :param key_len: the length of the hidden part of the key
    :return: the hidden part of the key
    """
    key = bytearray([3, 255, 0])
    for a in range(key_len):
        key[0] = a + 3
        possible = Counter()
        for x in trange(256):
            key[2] = x
            c = encrypt_oracle(key[:3], b"\x00")
            possible[_possible_key_bit(key, c)] += 1
        key.append(possible.most_common(1)[0][0])
        print(key[3:])
    # return key[3:]


attack(get_encrypted, 50)
# if b'crypto{' in key:
# 	print(key)
# 	break
# flag_len += 1