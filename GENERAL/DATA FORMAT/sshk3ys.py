from Crypto.PublicKey import RSA

f = open("D:\Save\Code\CTF\CRYPTOHACK\GENERAL\DATA FORMAT\RSA.pem", "r")
key = f.read()
enc = RSA.importKey(key)
print(enc.n)