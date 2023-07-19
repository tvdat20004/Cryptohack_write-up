from Crypto.PublicKey import RSA
from Crypto.Util.number import bytes_to_long as b2l
with open('transparency_afff0345c6f99bf80eab5895458d8eab.pem', 'r') as f:
    contents = RSA.importKey(f.read())
print(contents)