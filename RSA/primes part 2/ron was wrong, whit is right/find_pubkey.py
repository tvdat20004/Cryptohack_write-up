from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Util.number import long_to_bytes
with open('21.pem') as f:
    key = RSA.importKey(f.read())
n = key.n
e = key.e
print("n = ",n)
print("e = ",e) 