#Cách 1
def extended_gcd(p,q):
    if p == 0:
        return (q, 0, 1)
    else:
        (gcd, u, v) = extended_gcd(q % p, p)
        return (gcd, v - (q // p) * u, u)
       
p = 3
q = 13
gcd, u, v = extended_gcd(p, q)
print("[+] GCD: {}".format(gcd))
print("[+] u,v: {},{}".format(u,v))

#Cách 2
from Crypto.Util.number import inverse

print(inverse(3, 13))