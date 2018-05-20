import os
import re

def count_cyrillic_dirs(start_path = '.'):
    cyrillic_names = 0
    
    for root, dirs, files in os.walk(start_path):
        for dir_name in dirs:
            if re.search('^[А-ЯЁ]+$', dir_name, flags = re.IGNORECASE):
                cyrillic_names += 1
            
    return cyrillic_names


cyrillic_names = count_cyrillic_dirs()
print(cyrillic_names)
            
