from Crypto.PublicKey import RSA
with open('key_17a08b7040db46308f8b9a19894f9f95.pem', 'r') as f:
    key_data = f.read()
key = RSA.import_key(key_data)
n = key.n
e = key.e
print("n = ", n)
print("e = ", e)