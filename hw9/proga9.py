import re

def text_from_file(filename):
    f = open(filename, 'r', encoding = 'utf-8')
    text = f.read()
    return text

def find_forms(text):
    forms1 = re.findall('["\s\n]?най[дт][иеёуя](?:те?|шь|м)?', text, flags = re.IGNORECASE)
    #print(forms1)
    forms2 = re.findall('["\s\n]?нашё?л[аио]?', text, flags = re.IGNORECASE)
    #print(forms2)
    forms3 = re.findall('["\s\n]?нашедш[еи](?:го|й|му?|е|х)', text, flags = re.IGNORECASE)
    #print(forms3)
    all_forms = forms1 + forms2 + forms3
    return all_forms

text = text_from_file('words.txt')
forms = find_forms(text)
for elem in forms:
    print(elem.strip(), end = ' ')