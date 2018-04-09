import re

def read_file():
    with open('Викинги.txt', 'r', encoding='utf-8') as f:
        file = f.read()
    return file

def change(file):
    file2 = re.sub(r'(\W)викинг([иаоуе]?[вмх]?и?)(\W)', r'\1бурундук\2\3', file)
    return file2

def make_file(file2):
    with open('Бурундуки.txt', 'w', encoding='utf-8') as f:
        f.write(file2)

file = read_file()
file2 = change(file)
make_file(file2)
