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
def find_embedding_degree(E,p):
    """
    E : Elliptic Curve
    p : the order of base ring
    """
    k = 1
    n = E.order()
    while (p**k - 1) % n != 0:
        k += 1
    return k

#MOV attack !!!
def MOV_attack(E, G, A, p):
    """
    E: Elliptic curve
    G: generator point
    A: Point = x*G
    p: the order of base ring
    """
    k = find_embedding_degree(E,p) 
    E2 = EllipticCurve(GF(p**k), [a,b])
    T = E2.random_point()
    M = T.order()
    N = G.order()
    T1 = (M//gcd(M, N)) * T
    _G = E2(G).weil_pairing(T1, N)
    _A = E2(A).weil_pairing(T1, N)
    nA = _A.log(_G)
    return nA

p = 1331169830894825846283645180581
a = -35
b = 98
E = EllipticCurve(GF(p), [a,b])
G = E(479691812266187139164535778017,568535594075310466177352868412)
A = E(1110072782478160369250829345256,800079550745409318906383650948)
B = E(1290982289093010194550717223760,762857612860564354370535420319)
iv = 'eac58c26203c04f68d63dc2c58d79aca'
encrypted_flag = 'bb9ecbd3662d0671fd222ccb07e27b5500f304e3621a6f8e9c815bc8e4e6ee6ebc718ce9ca115cb4e41acb90dbcabb0d'
n = MOV_attack(E,G,A,p)
# n = 29618469991922269
assert n*G == A 
shared_secret = (n * B).xy()[0]
print(decrypt_flag(shared_secret, iv, encrypted_flag))
