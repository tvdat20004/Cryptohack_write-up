from sage.all import * 
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
import json 
p = 13322168333598193507807385110954579994440518298037390249219367653433362879385570348589112466639563190026187881314341273227495066439490025867330585397455471

def load_matrix(fname):
    data = open(fname, 'r').read().strip()
    rows = [list(map(int, row.split(' '))) for row in data.splitlines()]
    return Matrix(GF(p), rows)

G = load_matrix("generator.txt")
given = json.loads(open("output.txt", "r").read())
v = vector(GF(p), given["v"])
w = vector(GF(p), given["w"])
a, b = G.jordan_form(transformation=True)
print(a)