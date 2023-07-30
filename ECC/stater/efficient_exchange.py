from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib
from sympy.ntheory import sqrt_mod
from sage.all import *
class Point:
    def __init__(self,x,y,p):
        F = GF(p)
        self.x = F(x)
        self.y = F(y)
        self.modulus = p

def addition(p1 : Point, p2: Point, a,b):
    x1 = p1.x
    x2 = p2.x
    y1 = p1.y
    y2 = p2.y

    if x1 == x2 and y1 == y2:
        lamda = (3*x1**2 + a) / (2*y1)
    else:
        lamda = (y2 - y1) / (x2 - x1)
    x = lamda**2 - x1 - x2
    y = lamda*(x1 - x) - y1
    return Point(x,y,p1.modulus)
def scalar_multiplication(p: Point, n,a,b):
    q = p
    r = 0
    while n > 0:
        if n % 2 == 1:
            try:
                r = addition(r,q,a,b)
            except:
                r = q
        q = addition(q,q,a,b)
        n = n//2
    return r 

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
x = 4726
n_b = 6534

[y1,y2] = sqrt_mod(x**3 + 497*x + 1768, 9739, True)
p1 = Point(x,y1,9739)
p2 = Point(x,y2,9739)
a1 = scalar_multiplication(p1,n_b,497,1768)
a2 = scalar_multiplication(p2,n_b,497, 1768)

shared_secret1 = a1.x
shared_secret2 = a2.x 

iv = 'cd9da9f1c60925922377ea952afc212c'
ciphertext = 'febcbe3a3414a730b125931dccf912d2239f3e969c4334d95ed0ec86f6449ad8'

print(decrypt_flag(shared_secret1, iv, ciphertext))
print(decrypt_flag(shared_secret2, iv, ciphertext))
