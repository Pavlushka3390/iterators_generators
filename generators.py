import hashlib

def get_md5(path):
    with open(path) as file:
        for line in file:
            yield hashlib.md5(line.encode()).hexdigest()

for elm in get_md5('wiki'):
    print(elm)
