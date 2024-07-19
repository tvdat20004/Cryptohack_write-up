from chacha20_c76e2a43164af8b6ecb0e145415ab931 import ChaCha20
iv1 = bytes.fromhex('e42758d6d218013ea63e3c49')
iv2 = bytes.fromhex('a99f9a7d097daabd2aa2a235')
msg_enc = bytes.fromhex('f3afbada8237af6e94c7d2065ee0e221a1748b8c7b11105a8cc8a1c74253611c94fe7ea6fa8a9133505772ef619f04b05d2e2b0732cc483df72ccebb09a92c211ef5a52628094f09a30fc692cb25647f')
flag_enc = bytes.fromhex('b6327e9a2253034096344ad5694a2040b114753e24ea9c1af17c10263281fb0fe622b32732')
msg = b'Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula.'
def rotate(x, n):
    return ((x << n) & 0xffffffff) | ((x >> (32 - n)) & 0xffffffff)

def word(x):
    return x % (2 ** 32)
def xor(a, b):
    return b''.join([bytes([x ^ y]) for x, y in zip(a, b)])
def bytes_to_words(b):
    return [int.from_bytes(b[i:i+4], 'little') for i in range(0, len(b), 4)]
def words_to_bytes(w):
    return b''.join([i.to_bytes(4, 'little') for i in w])

key_stream = bytes_to_words(xor(msg[:64], msg_enc[:64]))

def inv_quarter_round(x, a, b, c, d):
    x[b] = rotate(x[b], 32 - 7); x[b] ^= x[c]; x[c] = word(x[c] - x[d])
    x[d] = rotate(x[d], 32 - 8); x[d] ^= x[a]; x[a] = word(x[a] - x[b])
    x[b] = rotate(x[b], 32 - 12); x[b] ^= x[c]; x[c] = word(x[c] - x[d])
    x[d] = rotate(x[d], 16); x[d] ^= x[a]; x[a] = word(x[a] - x[b])

def quarter_round(x, a, b, c, d):
    x[a] = word(x[a] + x[b]); x[d] ^= x[a]; x[d] = rotate(x[d], 16)
    x[c] = word(x[c] + x[d]); x[b] ^= x[c]; x[b] = rotate(x[b], 12)
    x[a] = word(x[a] + x[b]); x[d] ^= x[a]; x[d] = rotate(x[d], 8)
    x[c] = word(x[c] + x[d]); x[b] ^= x[c]; x[b] = rotate(x[b], 7)
def inv_inner_block(state):
    inv_quarter_round(state, 3, 4, 9, 14)
    inv_quarter_round(state, 2, 7, 8, 13)
    inv_quarter_round(state, 1, 6, 11, 12)
    inv_quarter_round(state, 0, 5, 10, 15)
    inv_quarter_round(state, 3, 7, 11, 15)
    inv_quarter_round(state, 2, 6, 10, 14)
    inv_quarter_round(state, 1, 5, 9, 13)
    inv_quarter_round(state, 0, 4, 8, 12)
def reverse_key_stream(key_stream):
    for i in range(10):
        inv_inner_block(key_stream)
    return key_stream

init_state = reverse_key_stream(list(key_stream))
key =words_to_bytes(init_state[4:12])
cipher = ChaCha20()
flag = cipher.decrypt(flag_enc, key, iv2)
print(flag)
