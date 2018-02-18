import random

def read_words(file):
    with open(file, 'r', encoding = 'utf-8') as f:
        lines = f.readlines()
    return lines
    
def create_dict(lines):
    hint = dict()
        
    for elem in lines:
        words = elem.split(';')
        hint[words[1]] = words[0]
        
    return hint

def choose_word(d):
    all_keys = list(d.keys())
    guessed_word = random.choice(all_keys)    
    return guessed_word

def start_print():
    global guessed_word
    dots = '.' * len(guessed_word)
    print('Угадайте пропущенное слово')
    print(hint[guessed_word], dots, sep = '', end = '')    
    
def check_if_right(user_answer):
    if user_answer == guessed_word.strip():
        print('Да, это так!')
    else:
        print('Нет, ну вы чего, совсем нет.')    
    
words_lines = read_words('words_hints.csv')    
hint = create_dict(words_lines)    
guessed_word = choose_word(hint)

start_print()
user_answer = input()

check_if_right(user_answer)
