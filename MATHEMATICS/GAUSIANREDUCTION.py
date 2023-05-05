import numpy   

u = numpy.array((87502093, 123094980))   

v = numpy.array((846835985, 9834798552))   

   

while True:   

    if numpy.linalg.norm(v) < numpy.linalg.norm(u):   

        u, v = v, u   

    m = u.dot(v) // u.dot(u)   

    if m == 0:   

        break   

    v = v - m * u   

   

   

print(u.dot(v)) 