import json
import encode

def load_file(path_to_file, password):
    with open(path_to_file) as f:
        encode_password = f.readline()
        lst_encode = json.load(f)
    lst_decode = []
    for i in lst_encode:
        j = {}
        for key, value in i.items():
            j[key] = encode.decode(password, value)
        lst_decode.append(j)
    return lst_decode

def save_file(path_to_file, lst_decode, password):
    lst_encode = []
    for i in lst_decode:
        j = {}
        for key, value in i.items():
            j[key] = encode.encode(password, value)
        lst_encode.append(j)
    with open(path_to_file, 'w') as f:
        f.write(f"{encode.encode(password, password)}\n")
        for i in json.dumps(lst_encode):
            f.write(i)
        f.close()


