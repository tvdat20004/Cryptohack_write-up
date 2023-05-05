#Cách 1
from pwn import*
enc = "label"
print(xor(enc, 13).decode())

#Cách 2
deff = 'label'
flag = []
flag_enc = []
for i in deff:
    flag.append(ord(i))
for i in flag:
    flag_enc.append(i ^ 13)
for i in flag_enc:
    print(chr(i))

