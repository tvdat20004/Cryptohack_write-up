from sage.all import *
import hashlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

def is_pkcs7_padded(message):
    padding = message[-message[-1]:]
    return all(padding[i] == len(padding) for i in range(0, len(padding)))

def decrypt_flag(shared_secret: int, iv: str, ciphertext: str):
    # Derive AES key from shared secret
    sha1 = hashlib.sha1()
    sha1.update(str(shared_secret).encode('ascii'))
    key = sha1.digest()[:16]
    # Decrypt flag
    ciphertext = bytes.fromhex(ciphertext)
    iv = bytes.fromhex(iv)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext)

    if is_pkcs7_padded(plaintext):
        return unpad(plaintext, 16).decode('ascii')
    else:
        return plaintext.decode('ascii')

p = 1331169830894825846283645180581
a = -35
b = 98
E = EllipticCurve(GF(p), [a,b])
print(E.order())
print(is_prime(E.order()))
G = E(479691812266187139164535778017,568535594075310466177352868412)
A = E(1110072782478160369250829345256,800079550745409318906383650948)
B = E(1290982289093010194550717223760,762857612860564354370535420319)
iv = 'eac58c26203c04f68d63dc2c58d79aca'
encrypted_flag = 'bb9ecbd3662d0671fd222ccb07e27b5500f304e3621a6f8e9c815bc8e4e6ee6ebc718ce9ca115cb4e41acb90dbcabb0d'
# n = G.discrete_log(A)
# print(n)