a = int(input("Нижний диапазон: "))
n = int(input("Верхний диапазон: "))
c = 0
for i in range(a, n + 1):
    i1 = True
    for j in range(2, i):
        if i % j == 0:
            i1 = False
            break
    if i1:
        c += 1
print("Найдено простых чисел: ", c)    