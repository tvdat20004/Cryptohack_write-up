import math
u1 = vector([846835985, 9834798552])
u2 = vector([87502093, 123094980])
while True:
	if u2.norm() < u1.norm():
		u1,u2 = u2,u1
	m = math.floor(float(u1*u2) / float(u1*u1))
	if m == 0: 
		print(u1,u2)
		break
	u2 = u2 - m*u1
print(u1*u2)
# (87502093, 123094980) (-4053281223, 2941479672)
# 7410790865146821
