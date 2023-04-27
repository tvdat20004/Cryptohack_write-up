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

A = 0xfffff
B = 0xccd6cd65c70a495a92ee3ad955daca0d4007d09f546ab048f2890a904f082999cb6c1ddbf3cd9515cfc3cd97cb77b60162d2718427153a4765c76c5f9672f5b01eaaeef1ec99de999867751531b66c39c63cba130ac47ffc77e1b4d24edb33224fe321ef28565d118d20ca1303aaef9adfe884ebb5385ef65449a7d91e347c940c6ea66ea1a31339fe3fd1dd6186d0b5932b3c2f92e1aef34cf96a2f7fb1eccafd5294504e8848b3a2cd38cd574d9282d7ecf0c9ecf98ad6bc5245ae17f596cb
p = 0xffffffffffffffffc90fdaa22168c234c4c6628b80dc1cd129024e088a67cc74020bbea63b139b22514a08798e3404ddef9519b3cd3a431b302b0a6df25f14374fe1356d6d51c245e485b576625e7ec6f44c42e9a637ed6b0bff5cb6f406b7edee386bfb5a899fa5ae9f24117c4b1fe649286651ece45b3dc2007cb8a163bf0598da48361c55d39a69163fa8fd24cf5f83655d23dca3ad961c62f356208552bb9ed529077096966d670c354e4abc9804f1746c08ca237327ffffffffffffffff
g = 0xf431bf57627b49de34bba7106ef3a3701eec16b42c38a93f78311b3741ad0bdd959a1fbb5a7054fdf6df0b651d0c50fd509d5aff1cbf81e1fcc24d61d1f1c0096a0a807d856502f4c8af2aaa0a2257a1f71591d65b7c21526d38315daf65794030434582b4919dd0575e9ef916fee5916bb228112b40ccab262c808c479ae46931479ff36476b5ed286b64442891e8bf59f227007c8cf0c20d5dde7699c2af8e122e75795e22fa53da55af1084ba7bb7548a1c601e1ca82a87b1faa8465e54ab

iv = "7d7a826e494511ac2ee5f75c2a5529d9"
ciphertext = "709c87b235f9c70a06cf0d9d83dd5d482113bde519d68c0ece4c1969cf9e7401"


shared_secret = B

print(decrypt_flag(shared_secret, iv, ciphertext))
