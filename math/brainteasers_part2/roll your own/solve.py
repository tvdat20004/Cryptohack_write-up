import math
from pwn import *
import json
# from sage import *
connect = remote("socket.cryptohack.org", 13403)
q = connect.recvline().decode().split('"')[1]
q = int(q[2:],16)
g = q + 1
n = q**2
data = connect.recvuntil(b': ')
send = {
	"g" : hex(g),
	"n" : hex(n)
}
send_json = json.dumps(send)
connect.sendline(send_json.encode())
h = connect.recvline().decode().split('"')[1]
p = int(h[2:],16)
# h = Integers(int(data[2:],16))

# x = h.log(Integers(g))
connect.recvuntil(b': ')
print((p-1) % q)
x = (p-1) // q
send = {"x" : hex(x)}
send = json.dumps(send)
connect.send(send.encode())
data = connect.recv(2048)
# print(x)
print(data)
connect.close()
# crypto{Grabbing_Flags_with_Pascal_Paillier}