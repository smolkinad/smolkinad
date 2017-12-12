count = 0
summ = 0
a = 0
mini = 0
maxi = 0
while a != "":
    a = input("Введите число: ")
    if a != "":
        count = count + 1
        summ = summ + int(a)
        if count == 1:
            mini = int(a)
            maxi = int(a)
        if int(a) < mini:
            mini = int(a)
        if int(a) > maxi:
            maxi = int(a)
print("Среднее арифметическое =", summ/count, "минимальное –", mini, "максимальное –", maxi)
