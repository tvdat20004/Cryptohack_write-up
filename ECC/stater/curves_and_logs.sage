class Point:
	def __init__(self,x,y,p):
		F = GF(p)
		self.x = F(x)
		self.y = F(y)
		self.modulus = p

def addition(p1 : Point, p2: Point, a,b):
	x1 = p1.x
	x2 = p2.x
	y1 = p1.y
	y2 = p2.y

	if x1 == x2 and y1 == y2:
		lamda = (3*x1**2 + a) / (2*y1)
	else:
		lamda = (y2 - y1) / (x2 - x1)
	x = lamda**2 - x1 - x2
	y = lamda*(x1 - x) - y1
	return Point(x,y,p1.modulus)
def scalar_multiplication(p: Point, n,a,b):
	q = p
	r = 0
	while n > 0:
		if n % 2 == 1:
			try:
				r = addition(r,q,a,b)
			except:
				r = q
		q = addition(q,q,a,b)
		n = n//2
	return r 


q = Point(815, 3190,9739)

a = scalar_multiplication(q,1829,497,1768)
import hashlib
print(hashlib.sha1(str(a.x).encode()).hexdigest())