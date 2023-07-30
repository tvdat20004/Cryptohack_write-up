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

# A = 0x561872a6a84b77dc623aaa73ebd9768618118ec2c07cd11ba4c34b9f6f4c610e1913f04275a7dd1ed3be718a62e5142e6cb7f0577b3ee94cc8f6db9b7cd1f73dedb9c638127f1209ca006264449ec321dfeca433e1797c2b964f6f45be88fe419052a877159cc477c7a2a6ac5f32d6eb0b25d2c4d057b7a227e1ccb08efcf9c2b793bb507bce1e0dcde52ab01e07bdf5a8002fbd46aa2842448da6eb15bc556281e3be5276b60b2bf76449219185dfd00339100c70be4e875f5e135044d218bb
# b = 197395083814907028991785772714920885908249341925650951555219049411298436217190605190824934787336279228785809783531814507661385111220639329358048196339626065676869119737979175531770768861808581110311903548567424039264485661330995221907803300824165469977099494284722831845653985392791480264712091293580274947132480402319812110462641143884577706335859190668240694680261160210609506891842793868297672619625924001403035676872189455767944077542198064499486164431451944
# p = 2410312426921032588552076022197566074856950548502459942654116941958108831682612228890093858261341614673227141477904012196503648957050582631942730706805009223062734745341073406696246014589361659774041027169249453200378729434170325843778659198143763193776859869524088940195577346119843545301547043747207749969763750084308926339295559968882457872412993810129130294592999947926365264059284647209730384947211681434464714438488520940127459844288859336526896320919633919

shared_secret = 1
iv = "3737f49155a59ca6b451026b0554d690"
ciphertext = "3bac0e6fadaaf85aaa2a5fa4538262ce018299ebb4aa9036b8736455b99936a2"

print(decrypt_flag(shared_secret, iv, ciphertext))