import re

def read_file(filename):
    with open(filename, 'r', encoding = 'utf-8') as f:
        lines = f.readlines()
    return lines

def find_time_zone(html_lines):
    for line in html_lines:
        if re.search('UTC[\+−-]\d+', line): # на страницах вики могут быть использованы другие символы для минуса
            print(re.search('UTC[\+−-]\d+', line).group())
            
find_time_zone(read_file('Санкт-Петербург.html'))
