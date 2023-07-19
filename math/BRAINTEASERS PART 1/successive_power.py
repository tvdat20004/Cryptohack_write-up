import sympy
pt = [588, 665, 216, 113, 642, 4, 836, 114, 851, 492, 819, 237]
prime = list(sympy.primerange(851,1000))
for p in prime:
	x = pt[1] * pow(pt[0],-1,p) % p
	if all(x == pt[i + 1] * pow(pt[i], -1, p) % p for i in range(1,len(pt) - 1)):
		print(p,x)
# 919 209
