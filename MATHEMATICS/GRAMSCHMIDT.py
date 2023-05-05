import numpy   

A = [numpy.array([4,1,3,-1]),   

     numpy.array([2,1,-3,4]),   

     numpy.array([1,0,-2,7]),   

     numpy.array([6,2,9,-5])]   

   

B = [A[0]]   

for i in range(1, 4):   

    mi = [numpy.dot(A[i],B[j]) / numpy.dot(B[j], B[j]) for j in range(len(B))]   

    B += [A[i] - sum([mij * Bj for (mij, Bj) in zip(mi, B)])]   

   

print(round(B[3][1], 5)) 