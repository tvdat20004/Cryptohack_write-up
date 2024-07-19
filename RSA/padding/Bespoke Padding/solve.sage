from Crypto.Util.number import long_to_bytes
import json 
from pwn import *
from sage.all import *
r = remote("socket.cryptohack.org", int(13386))
r.recvuntil(b'\n')

def get_para():
	send = json.dumps({"option" : "get_flag"})
	r.sendline(send.encode())
	data = json.loads(r.recvuntilS(b'\n'))

	enc = data["encrypted_flag"]
	n = data["modulus"]
	a,b = data["padding"]
	return enc, n, a, b 
enc1, n,a1,b1 = get_para()
enc2, n,a2,b2 = get_para()
r.close()
P.<x> = PolynomialRing(Zmod(n))
f1 = (a1*x + b1)^11 - enc1
f2 = (a2*x + b2)^11 - enc2
def gcd_zmod(f, g):
    while g:
        f, g = g, f % g
    return f
f = gcd_zmod(f1,f2).monic()
m = f.coefficients()[0]
print(long_to_bytes(int(-m)))