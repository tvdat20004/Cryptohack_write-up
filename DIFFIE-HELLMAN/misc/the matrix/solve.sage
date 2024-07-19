N = 50
E = 31337
FLAG = b'crypto{??????????????????????????}'

def load_matrix(fname):
    data = open(fname, 'r').read().strip()
    rows = [list(map(int, row)) for row in data.splitlines()]
    return Matrix(GF(2), rows)

def recover_plaintext(mat):
    temp = ""
    for i in range(N):
        for j in range(N):
            temp = temp + str(mat[j][i])

    temp = temp[:len(FLAG) * 8]
    return int(temp, 2).to_bytes((len(temp) + 7) // 8, 'big')

mtx = load_matrix('flag_403b981c77d39217c20390c1729b15f0.enc')
d = pow(E, -1, mtx.multiplicative_order())
mat = mtx ^ d

flag = recover_plaintext(mat)
print(flag)