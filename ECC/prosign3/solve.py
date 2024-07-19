from datetime import datetime 
from pwn import *
from json import loads, dumps
from ecdsa.ecdsa import generator_192, Public_key, Private_key
from hashlib import sha1 
from Crypto.Util.number import bytes_to_long

g = generator_192
n = g.order()
connect = remote("socket.cryptohack.org", 13381)
connect.recvline()

def get_signature():
	payload = {"option" : "sign_time"}
	connect.sendline(dumps(payload).encode())
	get = loads(connect.recvlineS())
	return get


sign = get_signature()

msg = sign["msg"]
r = int(sign["r"][2:],16)
s = int(sign["s"][2:],16)

for nonce in range(1,60):
	R = (g*nonce).x()
	if R == r:
		break
print(nonce)
h = bytes_to_long(sha1(msg.encode()).digest())
secret = (s*nonce - h) * pow(r,-1,n) % n 
pubkey = Public_key(g,g*secret)
privkey = Private_key(pubkey, secret)
new_hash = bytes_to_long(sha1(b"unlock").digest())
new_sig = privkey.sign(new_hash, nonce)

new_r = new_sig.r 
new_s = new_sig.s 
sub = {"option" : "verify", "msg" : "unlock", "r" : str(r), "s" : str(s)}
connect.sendline(dumps(sub).encode())
flag = connect.recvlineS()
print(flag)