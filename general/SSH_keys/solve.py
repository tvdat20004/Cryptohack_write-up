from Crypto.PublicKey import RSA
from Crypto.Util.number import bytes_to_long as b2l
with open('bruce_rsa_6e7ecd53b443a97013397b1a1ea30e14.pub', 'r') as f:
    contents = RSA.importKey(f.read())
print(contents.n)