import os
import re

neighbours = os.listdir()
without_nums = 0
for name in neighbours:
    if not re.search('[0-9]', name):
        without_nums += 1
        
print('Найдено {} файлов и папок без цифр в названии.'.format(without_nums))
print('Список всех найденных файлов и папок:')
print('\n'.join(set(neighbours)))
