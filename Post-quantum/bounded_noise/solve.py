from sage.all import *
import json

# Given parameters
q = 0x10001

# Load A and b from output.txt
with open("output_82aed503c474858718e4d34cfbd06cff.txt", "r") as f:
    data = json.load(f)
A = Matrix(GF(q), eval(data['A']))
b = vector(GF(q), eval(data['b']))

# Dimensions
n, m = A.ncols(), A.nrows()

# Construct the lattice basis
B = Matrix(ZZ, m + n + 1, m + n + 1)
B[:m, :n] = q * Matrix(ZZ, A)
B[:m, n:n + m] = Matrix(ZZ, m)
B[:m, -1] = vector(ZZ, b)
B[m:m + n, :n] = q * Matrix.identity(ZZ, n)
B[m + n, -1] = q

# Applying LLL to the basis matrix B
B = B.LLL()

# Extract the secret key
candidate = B[0, :n]
secret_key = vector(GF(q), candidate[:n])
# Convert the secret key back to the FLAG
flag_int = 0
for i in reversed(range(len(secret_key))):
    flag_int = flag_int * q + int(secret_key[i])

FLAG = flag_int.to_bytes((flag_int.bit_length() + 7) // 8, "big")
print(FLAG.decode())