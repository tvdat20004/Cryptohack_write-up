from decimal import *
import math
from sage.all import *
getcontext().prec = int(100)
PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103]
coeffs = []
for i in PRIMES:
    coeffs.append(int(math.floor(Decimal(int(i)).sqrt()*int(16**64))))

ct = 1350995397927355657956786955603012410260017344805998076702828160316695004588429433
mat = [
    [0 for j in range(len(PRIMES) + 1)] for i in range(len(PRIMES) + 1)
]

mat[0][0] = ct 
for i in range(len(PRIMES)) :
    mat[0][i + 1] = -coeffs[i]
    mat[i + 1][i + 1] = 1 

mat = matrix(mat).transpose()
mat = mat.LLL()
print(mat)
for row in mat:
    ok = list([abs(i) for i in row[1:]])
    wtf = False
    for i in ok:
        if i >=256:
            wtf = True
            break

    if not wtf:
        print(ok)

        print(bytes(ok))