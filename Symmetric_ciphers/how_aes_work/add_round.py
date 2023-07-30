state = [
    [206, 243, 61, 34],
    [171, 11, 93, 31],
    [16, 200, 91, 108],
    [150, 3, 194, 51],
]

round_key = [
    [173, 129, 68, 82],
    [223, 100, 38, 109],
    [32, 189, 53, 8],
    [253, 48, 187, 78],
]

def add_round_key(s, k):
    flag = b''
    for i in range(4):
        for j in range(4):
            flag += (s[i][j]^k[i][j]).to_bytes()
    return flag


print(add_round_key(state, round_key))

# crypto{r0undk3y}