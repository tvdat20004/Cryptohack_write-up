p = 0xde26ab651b92a129
g = 0x2
A = 0x3f8a592abb1225c0
# a = 7102201237866502329  
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib


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

B = 0x612243baa46489a9
R = Integers(p)
g = R(g)
a = R(A).log(g)
print(a)
shared_secret = pow(B,a,p)
iv = "4618b843f64abd17943bd27cf43fc358"
ciphertext = "4525015947f45e1e69239b760cd0b71b53ef243c19780eef3f29e1838f4bb009"

print(decrypt_flag(shared_secret, iv, ciphertext))

