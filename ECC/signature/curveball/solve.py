from sage.all import *
from json import loads,dumps
from pwn import *

# get P256 parameters at https://neuromancer.sk/std/nist/P-256
p = 0xffffffff00000001000000000000000000000000ffffffffffffffffffffffff
a = 0xffffffff00000001000000000000000000000000fffffffffffffffffffffffc

b = 0x5ac635d8aa3a93e7b3ebbd55769886bc651d06b0cc53b0f63bce3c3e27d2604b
E = EllipticCurve(GF(p),[a,b])
G = E(0x6B17D1F2E12C4247F8BCE6E563A440F277037D812DEB33A0F4A13945D898C296,0x4FE342E2FE1A7F9B8EE7EB4A7C0F9E162BCE33576B315ECECBB6406837BF51F5)
n = E.order()
assert n == 0xffffffff00000000ffffffffffffffffbce6faada7179e84f3b9cac2fc632551

pub = E(0x3B827FF5E8EA151E6E51F8D0ABF08D90F571914A595891F9998A5BD49DFA3531, 0xAB61705C502CA0F7AA127DEC096B2BBDC9BD3B4281808B3740C320810888592A)
d = 2
while gcd(d,n) > 1:
	d += 1
Q = pub * int(pow(d,-1,n))
print(Q)
assert Q*d == pub 
r = remote("socket.cryptohack.org", 13382)
payload = {
	"private_key" : int(d),
	"host" : "www.bing.com",
	"curve" : "secp256r1",
	"generator" : (int(Q.xy()[0]),int(Q.xy()[1])),
}
payload = dumps(payload)
data = r.recvuntil(b'\n')
r.sendline(payload.encode()	)
r.interactive()
