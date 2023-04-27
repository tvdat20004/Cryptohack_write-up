def order(g, p):
	for i in range(2, p):
		if pow(g, i, p) == g:
			return i
	return p
		
p = 28151
for g in range(2,p):
	if p == order(g,p): 
		print(g) 
		break