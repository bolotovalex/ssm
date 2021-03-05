from base64 import urlsafe_b64decode, urlsafe_b64encode

def encode(key, str):
    enc = []
    enc.clear()
    for i in range(len(str)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(str[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return urlsafe_b64encode("".join(enc).encode()).decode()

def decode(key, enc):
    dec = []
    dec.clear()
    enc = urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)

def encode_key(passwd, file):
    encode_file = ''
    pass
    return encode_file

def decode_key(passwd, file):
    decode_file = ''
    pass
    return decode_file