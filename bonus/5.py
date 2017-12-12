word = input("Введите слово: ")
word = list(word)
res = []
for letter in word:
    if letter == "q" or letter == "r" or letter == "t" or letter == "p" or letter == "s" or letter == "d" or letter == "f" or letter == "g" or letter == "h" or letter == "j" or letter == "k" or letter == "l" or letter == "z" or letter == "x" or letter == "c" or letter == "v" or letter == "b" or letter == "n" or letter == "m":
        res.append(letter)
        res.append("aig")
    else:
        res.append(letter)
print(res)
