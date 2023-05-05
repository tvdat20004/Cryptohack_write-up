s = [588, 665, 216, 113, 642, 4, 836, 114, 851, 492, 819, 237]   

   

pmn = max(s) + 1   

   

for p in range(pmn, 1000):   

    x = [(s[i] * inverse(s[i - 1], p)) % p for i in range(1, 12)]   

    if(len(set(x)) == 1):   

        print(x, p)   

        break   