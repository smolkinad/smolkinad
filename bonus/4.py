word = input("Введите слово: ")
word = list(word)
res = []
for letter in word:
    if letter == "а" or letter == "о" or letter == "е" or letter == "у" or letter == "и" or letter == "я" or letter == "э" or letter == "ю" or letter == "ы":
        res.append(letter)
        res.append("c")
        res.append(letter)
    else:
        res.append(letter)
print(res
