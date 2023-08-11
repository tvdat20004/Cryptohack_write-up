from sage.all import *
from Crypto.Util.number import long_to_bytes

p = 4368590184733545720227961182704359358435747188309319510520316493183539079703
F = GF(p)

gx = F(8742397231329873984594235438374590234800923467289367269837473862487362482)
gy = F(225987949353410341392975247044711665782695329311463646299187580326445253608)
x = F(2582928974243465355371953056699793745022552378548418288211138499777818633265)
y = F(2421683573446497972507172385881793260176370025964652384676141384239699096612)

t1 = gy**2 - gx**3
t2 = y**2 - x**3
a = (t1-t2) / (gx - x)
b = t1 - a*gx


def attack(p, a2, a4, a6, Gx, Gy, Px, Py):
    """
    Solves the discrete logarithm problem on a singular curve (y^2 = x^3 + a2 * x^2 + a4 * x + a6).
    :param p: the prime of the curve base ring
    :param a2: the a2 parameter of the curve
    :param a4: the a4 parameter of the curve
    :param a6: the a6 parameter of the curve
    :param Gx: the base point x value
    :param Gy: the base point y value
    :param Px: the point multiplication result x value
    :param Py: the point multiplication result y value
    :return: l such that l * G == P
    """
    x = GF(p)["x"].gen()
    f = x ** 3 + a2 * x ** 2 + a4 * x + a6
    roots = f.roots()

    # Singular point is a cusp.
    if len(roots) == 1:
        alpha = roots[0][0]
        u = (Gx - alpha) / Gy
        v = (Px - alpha) / Py
        return int(v / u)

    # Singular point is a node.
    if len(roots) == 2:
        if roots[0][1] == 2:
            alpha = roots[0][0]
            beta = roots[1][0]
        elif roots[1][1] == 2:
            alpha = roots[1][0]
            beta = roots[0][0]
        else:
            raise ValueError("Expected root with multiplicity 2.")

        t = (alpha - beta).sqrt()
        u = (Gy + t * (Gx - alpha)) / (Gy - t * (Gx - alpha))
        v = (Py + t * (Px - alpha)) / (Py - t * (Px - alpha))
        return int(v.log(u))

    raise ValueError(f"Unexpected number of roots {len(roots)}.")

flag = attack(p,0,a,b,gx,gy,x,y)
print(long_to_bytes(flag))