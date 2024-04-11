#Задание №7
n = int(input())
max=0
while n > 0:
    razrad = n % 10
    if razrad % 2 == 0 and razrad>max:
        max=razrad
    n=n//10    
print(max)