import random

with open('words_hints.csv', 'r', encoding = 'utf-8') as f:
    lines = f.readlines()
    
hint = dict()
    
for elem in lines:
    words = elem.split(';')
    hint[words[1]] = words[0]
    
all_keys = list(hint.keys())
guessed_word = random.choice(all_keys)
dots = '.' * len(guessed_word)

print('Угадайте второе слово')
print(hint[guessed_word], dots, sep = '', end = '')
user_answer = input()

if user_answer == guessed_word.strip():
    print('Да, это так!')
else:
    print('Ну вы что, ну нет же')
