import random


#открываем файлы



with open("C:/Users/smolk/Desktop/proga/adj_f.txt", encoding="utf-8") as f:
    part=f.read()
part=part.replace("\ufeff","")
adj_f=part.split(', ')

with open("C:/Users/smolk/Desktop/proga/adj_m.txt", encoding="utf-8") as f:
    part=f.read()
part=part.replace("\ufeff","")
adj_m=part.split(', ')

with open("C:/Users/smolk/Desktop/proga/noun_m.txt", encoding="utf-8") as f:
    part=f.read()
part=part.replace("\ufeff","")
noun_m=part.split(', ')

with open("C:/Users/smolk/Desktop/proga/noun_f.txt", encoding="utf-8") as f:
    part=f.read()
part=part.replace("\ufeff","")
noun_f=part.split(', ')

with open("C:/Users/smolk/Desktop/proga/verb.txt" ,encoding="utf-8") as f:
    part=f.read()
part=part.replace("\ufeff","")
verb=part.split(', ')

with open("C:/Users/smolk/Desktop/proga/punc.txt" ,encoding="utf-8") as f:
    part=f.read()
part=part.replace("\ufeff","")
punc=part.split('| ')



#пишем функции

def noun_f_func():
    
    return random.choice(noun_f)

def noun_m_func():
 
    return random.choice(noun_m)

def adj_m_func():
 
    return random.choice(adj_m)
def adj_f_func():
 
    return random.choice(adj_f)
def verb_func():
 
    return random.choice(verb)

def punc_func():
    
    return random.choice(punc)

#написали функции отдельных слов и пунктуации
#теперь соединяем это всё в словосочетания/фразы

def adj_f_noun_f_verb():
    return adj_f_func() + ' ' + noun_f_func() + ' ' + verb_func() + punc_func()

def adj_m_noun_m_verb():
    return adj_m_func() + ' ' + noun_m_func() + ' ' + verb_func() + punc_func()

def verb_adj_f_noun_f():
    return verb_func() + ' ' + adj_f_func() + ' ' + noun_f_func() + punc_func()

def verb_adj_m_noun_m():
    return verb_func() + ' ' + adj_m_func() + ' ' + noun_m_func() + punc_func()

def noun_f_adj_f_verb():
    return noun_f_func() + ' ' + adj_f_func() + ' ' + verb_func() + punc_func()

def noun_m_adj_m_verb():
    return noun_m_func() + ' ' + adj_m_func() + ' ' + verb_func() + punc_func()


def verse1():

    verse1a=[adj_f_noun_f_verb(), adj_m_noun_m_verb()]
    return random.choice(verse1a)

def verse2():
    verse2a=[verb_adj_f_noun_f(), verb_adj_m_noun_m()]
    return random.choice(verse2a)

def verse3():

    verse3a=[noun_f_adj_f_verb(), noun_m_adj_m_verb()]
    return random.choice(verse3a)

def verse4():

    verse4a=[verb_adj_m_noun_m(), adj_m_noun_m_verb()]
    return random.choice(verse4a)

def make_verse():
    print(verse1())
    print(verse2())
    print(verse3())
    print(verse4())
 
    

#а вот лютый основной код 

make_verse()
