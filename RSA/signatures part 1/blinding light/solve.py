from pwn import *
from Crypto.Util.number import *
import json
r = remote("socket.cryptohack.org" ,13376)

token = "admin=True"
r.recvuntil(b'\n')

def get_pubkey():
	send = {"option" : "get_pubkey"}
	send = json.dumps(send).encode()
	r.sendline(send)
	data = r.recvuntilS(b'\n')
	n = int(json.loads(data)["N"][2:],16)
	e = int(json.loads(data)["e"][2:],16)
	return n,e 
def sign():
	pt = bytes_to_long(token.encode())*pow(2,e,n) % n 
	send = {"option" : "sign", "msg" : hex(pt)[2:]}
	r.sendline(json.dumps(send).encode())
	data = r.recvuntilS(b'\n')
	sig = json.loads(data)["signature"][2:]
	return int(sig,16)
def verify(send_sig):
	send = {"option" : "verify", "msg" : token.encode().hex(), "signature" : hex(send_sig)[2:]}
	r.sendline(json.dumps(send).encode())
	data = r.recvuntilS(b'\n')
	print(data)

n, e = get_pubkey()
sig = sign()
send_sig = sig * pow(2,-1,n) % n 
verify(send_sig)
# crypto{m4ll34b1l17y_c4n_b3_d4n63r0u5}	
r.close()