import re

fname = input('Имя вашего файла: ' + ' ')
with open(fname, 'r', encoding='utf-8') as f:
    
    slova = f.read()
    
searching = re.search('<body>[0-9a-zа-я<>\\\/\s=",\-()|]*<\/body>', slova, flags = re.IGNORECASE).group()
counter = len(searching.strip('</>body'))

another_fname = input('Имя нового файла: ' + ' ')
with open(another_fname, 'w', encoding="utf-8") as f:
    newfile = f.writelines(print(counter))
