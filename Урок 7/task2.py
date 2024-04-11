n = int(input())
sum = 0
for i in range(1, n+1):
    f = 1
    for j in range(1, i+1):
        f = f * j
        print('i = ', i, ' j = ', j,' f = ', f, 'sum = ', sum )
    sum = sum + f
print(sum)    