from pwn import *
from json import * 
from Crypto.Cipher import AES
from Crypto.Util.number import bytes_to_long
r = remote("socket.cryptohack.org", 13399)
r.recvline()
def reset_password(token):
	pl_json = {
		"option" : "reset_password",
		"token" : token.hex()
	}
	r.sendline(dumps(pl_json).encode())
	recv = loads(r.recvlineS())


def authenticate(password):
	pl_json = {
		"option" : "authenticate",
		"password" : password.decode()
	}
	r.sendline(dumps(pl_json).encode())
	recv = loads(r.recvlineS())
	if recv["msg"] != "Wrong password.":
		print(recv)
		return True
	return False

def reset_connection():
	pl_json = {
		"option" : "reset_connection"
	}
	r.sendline(dumps(pl_json).encode())
	recv = loads(r.recvlineS())

while True:
	reset_password(b'0'*28)
	reset_connection()
	for i in range(32, 127):
		token = bytes([i])*12
		new_password = token[:-4]
		password_length = bytes_to_long(token[-4:])
		password = new_password[:password_length]
		if authenticate(password):
			quit()
