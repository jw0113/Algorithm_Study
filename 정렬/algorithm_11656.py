a = list(input())
result = [a[i:] for i in range(len(a))]
result.sort()
for i in range(len(a)):
    for j in range(len(result[i])):
        print(result[i][j], end='')
    print('')
