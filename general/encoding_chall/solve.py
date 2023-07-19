import socket, json
import base64
import codecs
from Crypto.Util.number import long_to_bytes
HOST = "socket.cryptohack.org"
PORT = 13377
def decode_base64(enc):
	return base64.b64decode(enc.encode()).decode()

def decode_hex(enc):
	return bytes.fromhex(enc).decode()

def decode_rot13(enc):
	return codecs.decode(enc, 'rot_13')
def decode_bigint(enc):
	return long_to_bytes(int(enc,16)).decode()
def decode_utf8(enc):
	dec = ""
	for i in enc:
		dec += chr(i)
	return dec

def decode_chall(encoding, enc):
	if encoding == "base64":
		decoded = decode_base64(enc)
	elif encoding == "hex":
		decoded = decode_hex(enc)
	elif encoding == "rot13":
		decoded = decode_rot13(enc)
	elif encoding == "bigint":
		decoded = decode_bigint(enc)
	elif encoding == "utf-8":
		decoded = decode_utf8(enc)
	return {"decoded" : decoded}


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.connect((HOST, PORT))
	data = s.recv(1024).decode()
	while "crypto" not in data:
		enc = json.loads(data)
		# print(enc)
		encoding = enc['type']
		print(enc)
		s.sendall(json.dumps(decode_chall(encoding,enc["encoded"])).encode())
		data = s.recv(1024).decode()
	s.close()
	print(data)
