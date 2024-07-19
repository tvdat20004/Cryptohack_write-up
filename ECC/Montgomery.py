# E: Y^2 = X^3 + 486662X^2 + X, p: 2^255 - 19
from sympy.ntheory import sqrt_mod 
from sage.all import GF
p = 2**255 - 19 
G_x = 9 
a = 486662 
F = GF(p)
class Point(object):
	"""docstring for Point"""
	def __init__(self, x,y):
		self.x = F(x)
		self.y = F(y)

	def __eq__(self, other):
		return self.x == other.x and self.y == other.y 

	def __add__(self, other):
		assert not (self == other)
		x1,y1 = self.x, self.y 
		x2,y2 = other.x, other.y 
		alpha = (y2 - y1) / (x2 - x1) 
		x3 = alpha**2 - a - x1 - x2 
		y3 = alpha*(x1 - x3) - y1 
		return Point(x3,y3)
	def double(self):
		x1,y1 = self.x, self.y 
		alpha = (3*x1**2 + 2*a*x1 + 1)/(2*y1)
		x3 = alpha**2 - a - 2*x1
		y3 = alpha*(x1 - x3) - y1
		return Point(x3,y3)

	def __mul__(self,k:int):
		ans = self
		r = 0 
		while k > 0:
			if k % 2 == 1:
				try:
					r = ans + r
				except:
					r = ans 
			ans = ans.double()
			k //= 2 

		return r

G_y2 = (G_x**3 + a*G_x**2 + G_x) % p 
G_y = sqrt_mod(G_y2,p)
G = Point(G_x, G_y) 

Q = G*0x1337c0decafe
print(Q.x)