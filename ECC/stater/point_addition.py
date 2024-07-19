from sage.all import GF
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
P = Point(493, 5564,9739)
Q = Point(1539, 4742,9739)
R = Point(4403,5202,9739)
x1 = addition(P,P,497,1768)
x2 = addition(x1,Q,497,1768)
x3 = addition(x2,R,497,1768)
assert x3.y**2 == x3.x**3 + 497*x3.x + 1768
print(x3.x, x3.y)
