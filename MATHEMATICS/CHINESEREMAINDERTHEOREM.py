from theorem import inverse   

def crt(a, m):   

    ans = 1   

    for i in m:   

        ans *= i   

    M = [ans // x for x in m]   

    y = [inverse(M[i], m[i]) for i in range(len(m))]   

    ans = 0   

    for i in range(len(m)):   

        total += a[i] * M[i] * y[i]   

    return total % ans   

print(crt([2,3,5], [5,11,17])) 