import json
from Crypto.Util.number import long_to_bytes

def decode_bigint(enc):
	return long_to_bytes(int(enc,16)).decode()
print(decode_bigint("0x656e7465727461696e6d656e745f656e67696e655f73746172746564"))