

# This file was *autogenerated* from the file solve.sage
from sage.all_cmdline import *   # import sage library

_sage_const_13403 = Integer(13403); _sage_const_1 = Integer(1); _sage_const_2 = Integer(2); _sage_const_16 = Integer(16)
import math
from pwn import *
import json
# from sage import *
connect = remote("socket.cryptohack.org", _sage_const_13403 )
q = connect.recvline().decode().split('"')[_sage_const_1 ]
q = int(q[_sage_const_2 :],_sage_const_16 )
g = q + _sage_const_1 
n = q**_sage_const_2 
data = connect.recvuntil(b': ')
send = {
	"g" : hex(g),
	"n" : hex(n)
}
send_json = json.dumps(send)
connect.sendline(send_json.encode())
data = connect.recvline().decode().split('"')[_sage_const_1 ]
h = Integers(int(data[_sage_const_2 :],_sage_const_16 ))

x = h.log(Integers(g))

print(x)

connect.close()

