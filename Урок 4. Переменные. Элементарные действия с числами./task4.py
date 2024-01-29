# задание 4
name = int(input())
# a - кол-во сотен
# b - кол-во десятков
# c - кол-во единиц 
if name<0:
    name = name*(-1)
a = name//100
b = name % 100 // 10
c = name % 10
print(name)
print(a*100+c*10+b)
print(b*100+a*10+c)
print(b*100+c*10+a)
print(c*100+a*10+b)
print(c*100+b*10+a)