import logging
from sage.all import GF, Matrix, crt
from sage.all import identity_matrix
from sage.matrix.matrix2 import _jordan_form_vector_in_difference
import json
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
P = 2 
N = 150
def load_matrix(fname):
    data = open(fname, 'r').read().strip()
    rows = [list(map(int, row)) for row in data.splitlines()]
    return Matrix(GF(P), rows)

def find_eigenvalues(A):
    """
    Computes the eigenvalues and P matrices for a specific matrix A.
    :param A: the matrix A.
    :return: a generator generating tuples of
        K: the extension field of the eigenvalue,
        k: the degree of the factor of the charpoly associated with the eigenvalue,
        e: the multiplicity of the factor of the charpoly associated with the eigenvalue,
        l: the eigenvalue,
        P: the transformation matrix P (only the first e columns are filled)
    """
    factors = {}
    for g, e in A.charpoly().factor():
        k = g.degree()
        if k not in factors or e > factors[k][0]:
            factors[k] = (e, g)

    p = A.base_ring().order()
    for k, (e, g) in factors.items():
        logging.debug(f"Found factor {g} with degree {k} and multiplicity {e}")
        K = GF(p ** k, "x", modulus=g, impl="modn" if k == 1 else "pari")
        l = K.gen()
        # Assuming there is only 1 Jordan block for this eigenvalue.
        Vlarge = ((A - l) ** e).right_kernel().basis()
        Vsmall = ((A - l) ** (e - 1)).right_kernel().basis()
        v = _jordan_form_vector_in_difference(Vlarge, Vsmall)
        P = identity_matrix(K, A.nrows())
        for i in reversed(range(e)):
            P.set_row(i, v)
            v = (A - l) * v

        P = P.transpose()
        yield K, k, e, l, P


def dlog(A, B):
    """
    Computes l such that A^l = B.
    :param A: the matrix A
    :param B: the matrix B
    :return: a generator generating values for l and m, where A^l = B mod m.
    """
    ls, ms = [], []
    assert A.is_square() and B.is_square() and A.nrows() == B.nrows()

    p = A.base_ring().order()
    for K, k, e, l, P in find_eigenvalues(A):
        B_ = P ** -1 * B * P
        logging.debug(f"Computing dlog in {K}...")
        ls.append(int(B_[0, 0].log(l)))
        ms.append(int(p ** k - 1))
        if e >= 2:
            B1 = B_[e - 1, e - 1]
            B2 = B_[e - 2, e - 1]
            ls.append(int((l * B2) / B1))
            ms.append(int(p ** k))
    return int(crt(ls, ms))
def derive_aes_key(M):
    mat_str = ''.join(str(x) for row in M for x in row)
    return SHA256.new(data=mat_str.encode()).digest()[:128]

G = load_matrix("generator.txt")
A_pub = load_matrix("alice.pub")
B_pub = load_matrix("bob.pub")
enc = json.loads(open("flag.enc", "r").read())
A_priv = dlog(G, A_pub)
shared_secret = B_pub ** A_priv
key = derive_aes_key(shared_secret)
cipher = AES.new(key, AES.MODE_CBC, bytes.fromhex(enc['iv']))
print(cipher.decrypt(bytes.fromhex(enc['ciphertext'])))

