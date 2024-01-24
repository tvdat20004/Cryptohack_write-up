from pkcs1 import emsa_pkcs1_v15
from Crypto.Util.number import * 
from pwn import * 
from json import * 
from sympy.ntheory import discrete_log
from sympy.ntheory.modular import crt
# from sage.all import * 

BIT_LENGTH = 768
def get_signature():
	payload = dumps({"option": "get_signature"})
	r.sendline(payload.encode())
	recv = loads(r.recvlineS())
	N = int(recv['N'][2:], 16)
	e = int(recv['E'][2:], 16)
	signature = int(recv['signature'][2:], 16)
	return N, e, signature

def set_pubkey(n):
	payload = dumps({"option" : "set_pubkey", "pubkey" : hex(n)[2:]})
	r.sendline(payload.encode())
	recv = loads(r.recvlineS())
	suffix = recv["suffix"]
	return suffix

def claim(msg, e, index):
	payload = dumps({"option" : "claim", "msg": msg, "e" : hex(e)[2:], "index": index})
	r.sendline(payload.encode())
	recv = loads(r.recvlineS())
	return bytes.fromhex(recv['secret'])

def gen_smooth(size):
	ans = 2
	while True:
		ans *= getPrime(20)
		# print(ans)
		if ans > size:
			if isPrime(ans+1):
				return ans
			else:
				ans = 2
				continue  


r = remote("socket.cryptohack.org", 13394)
r.recvline()
N,E, signature = get_signature()
n = getPrime(20)**40
 
suffix = set_pubkey(n)
btc_addr = "1F1tAaz5x1HUXrCNLbtMDqcw6o5GNn4xqX"
msg1 = "This is a test for a fake signature." + suffix
msg2 = "My name is dat and I own CryptoHack.org" + suffix
msg3 = "Please send all my money to " + btc_addr + suffix

digest1 = bytes_to_long(emsa_pkcs1_v15.encode(msg1.encode(), BIT_LENGTH // 8))
digest2 = bytes_to_long(emsa_pkcs1_v15.encode(msg2.encode(), BIT_LENGTH // 8))
digest3 = bytes_to_long(emsa_pkcs1_v15.encode(msg3.encode(), BIT_LENGTH // 8))

e1 = discrete_log(n, digest1, signature)
e2 = discrete_log(n, digest2, signature)
e3 = discrete_log(n, digest3, signature)
secrets = []
assert pow(signature, e1, n) == digest1
secrets.append(claim(msg1, e1, 0))
secrets.append(claim(msg2, e2, 1))
secrets.append(claim(msg3, e3, 2))
print(xor(xor(secrets[2], secrets[1]), secrets[0]))
# crypto{let's_decrypt_w4s_t0o_ez_do_1t_ag41n}