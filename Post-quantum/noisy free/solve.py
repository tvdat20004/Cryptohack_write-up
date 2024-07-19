from pwn import *
import json 
from tqdm import trange
from sage.all import * 
r = remote("socket.cryptohack.org", 13411)
r.recvline()
n = 64
p = 257
q = 0x10001
V = VectorSpace(GF(q), n)
def send_request(m, get_flag = True):
	if get_flag:
		js = {"option" : "get_flag", "index" : m}
	else:
		js = {"option" : "encrypt", "message" : m }

	r.sendline(json.dumps(js).encode())
	recv = r.recvlineS().strip()
	js_recv = json.loads(recv)
	A = eval(js_recv["A"])
	b = eval(js_recv["b"])
	return A, b 
def decrypt(A, b):
	return b - V(A) * S

mtx = []
ans = []
for i in trange(64):
	A, b = send_request(0, get_flag=False)
	ans.append(b)
	mtx.append(A)
mtx = Matrix(GF(q), mtx)
ans = V(ans)
S = V((~mtx) * ans)
index = 0
flag = b""
while True:
	try:
		char = int(decrypt(*send_request(index)))	
		flag += bytes([char])
		index += 1
	except:
		print(flag)
		quit()

