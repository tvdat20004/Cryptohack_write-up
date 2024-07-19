from pwn import *
from tqdm import trange
import json
from Crypto.Util.Padding import unpad
r = remote('socket.cryptohack.org', 13421)
# r = remote('127.0.0.1', 13421)
def padding_oracle(c):
    data = json.dumps({
        "option" : "unpad",
        "ct" : c.hex()
        })
    r.sendline(data.encode())
    recv = json.loads(r.recvlineS().strip())
    return recv['result']

def submit(msg):
    data = json.dumps({
        "option" : "check",
        "message" : msg
        })
    r.sendline(data.encode())
    print(r.recvlineS())

def get_ct():
    data = json.dumps({
        "option" : "encrypt"
        })
    r.sendline(data.encode())
    ct = bytes.fromhex(json.loads(r.recvlineS().strip())['ct'])
    return ct[:16], ct[16:]
def find_flag(iv, c):
    blocks = [c[i:i+16] for i in range(0,len(c),16)]

    msg = b''
    for b in range(len(blocks)-1,-1,-1):
        block_pt = b''
        i2 = [None] * 16
        pad = 1
        for i in range(15,-1,-1):
            for x in trange(256):
                valid_pad = b''
                t = 0
                while i + 1 + t != 16:
                    valid_pad = (i2[15 - t] ^ pad).to_bytes() + valid_pad
                    t += 1
                test = b'\x00'*i + x.to_bytes() + valid_pad + blocks[b]
                if padding_oracle(test):
                    i2[i] = x ^ pad
                    if b > 0:
                        block_pt = (blocks[b-1][i] ^ i2[i]).to_bytes() + block_pt
                    else:
                        block_pt = (iv[i] ^ i2[i]).to_bytes() + block_pt
                    break
            pad += 1
        msg = block_pt + msg
    return msg
# print(r.recvlineS())
r.recvlineS()
msg = find_flag(*get_ct())
submit(msg.decode())
r.close()
