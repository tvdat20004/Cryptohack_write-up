from sage.all import *
from Crypto.Cipher import AES
import hashlib
from Crypto.Util.Padding import pad, unpad

p = 99061670249353652702595159229088680425828208953931838069069584252923270946291
F = GF(p)
E = EllipticCurve(F,[1,4])
def find_priv_key(max_val,A,G):
	order = G.order()

	subresults = []
	factors = []
	modulus = 1
	for prime, exponent in factor(order):
	    if modulus >= max_val: break
	    _factor = prime ** exponent
	    factors.append(_factor)
	    G2 = G*(order//_factor)
	    A2 = A*(order//_factor)
	    subresults.append(discrete_log_lambda(A2, G2, bounds=(0,_factor), operation='+'))
	    modulus *= _factor

	n = crt(subresults,factors)
	assert(n * G == A)
	return n
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

G = E(43190960452218023575787899214023014938926631792651638044680168600989609069200,20971936269255296908588589778128791635639992476076894152303569022736123671173)

xA = F(87360200456784002948566700858113190957688355783112995047798140117594305287669)
xB = F(6082896373499126624029343293750138460137531774473450341235217699497602895121)
A = E.lift_x(xA)
B = E.lift_x(xB)
iv = 'ceb34a8c174d77136455971f08641cc5'
encrypted_flag = 'b503bf04df71cfbd3f464aec2083e9b79c825803a4d4a43697889ad29eb75453'
na = find_priv_key(2**64, A, G)
shared_secret = (B*na).xy()[0]
print(decrypt_flag(shared_secret, iv, encrypted_flag))
