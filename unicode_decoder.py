import sys
def decode_utf8(s: str) -> str:
    with open(s, 'rb') as f:
        data = f.read()
    text = data.decode('unicode_escape')
    return text    

def decode(path: str):
    decoded = decode_utf8(path)
    with open(f"{path}_d",encoding="utf-8",mode="x") as f:
        f.write(decoded)
    return True

if __name__ == "__main__":
    if len(sys.argv) < 2: raise ValueError('Please write path to file')
    else: status = decode(sys.argv[1])
    print(f'{"Succesed" if status else "Error"}')
