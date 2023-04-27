from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Util.number import inverse
import hashlib
from sympy.ntheory.residue_ntheory import discrete_log

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
        return unpad(plaintext, 16).decode('utf-8')
    else:
        return plaintext.decode('utf-8')
p = 0xffffffffffffffffc90fdaa22168c234c4c6628b80dc1cd129024e088a67cc74020bbea63b139b22514a08798e3404ddef9519b3cd3a431b302b0a6df25f14374fe1356d6d51c245e485b576625e7ec6f44c42e9a637ed6b0bff5cb6f406b7edee386bfb5a899fa5ae9f24117c4b1fe649286651ece45b3dc2007cb8a163bf0598da48361c55d39a69163fa8fd24cf5f83655d23dca3ad961c62f356208552bb9ed529077096966d670c354e4abc9804f1746c08ca237327ffffffffffffffff
A = 0xbd3335a6b131db963c905be2fc3377eae7507953602d38d32ae8517ea6ff82b9fa6185be0979dc68f594bb66557ede252d531572741c83fd807f8e2ece2a5e79c67a37da5672bbeca151805c0b00d9eb44631a936dafac98d2b4eada7de734022bb02a72ca1b7de56393fe30352cad33403ff803f065c8a30e535a2bf1b5c5c085052229a249b0d06d2a728d47170323c2e2b15d6e811864075cd4723bad3c29489e0e8ac39b79ab9a8e2f802d255f14e65508c402126ed151c335c518723824
g = 0x2
a = A * inverse(g, p)
B = 0x1e9d4e713c4855ea0679ad0107c93c6d5d456b397a174feddb0c57472daba607bdfe963e98183f3d07cfd7d4fe921c58a69a55c75ad3fca3731711dab81905e84dfec011baf4698bf57a19a0dba3d3c825f7a465590c58d7ca054da5226486f856ff1fdf9428aea5355f422b1e999509409c5cd75b3fa32db9007f4459174bae07e1ed85f4f53e91a4d3c2822fbc50f25e01d7bed7ca8c2c4cc26b238bc0065edfac448011145303dd5fe910bc0e75963c1bd53d4d9380835b804b5ac8ac89a9

shared_secret = (a * B) % p

iv = "f7d07e8b369318c158632599ce309981"
ciphertext = "e3fb61f033db68bdd8ad18b8e41c1d097a144a0bf338aa959c65a4d5b5ea5f4fb630d53f222b410766080f2f0e157694"

print(decrypt_flag(shared_secret, iv, ciphertext))