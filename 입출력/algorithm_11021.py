x = int(input())
count = 0
result = []
while count < x:
    a,b = map(int, input().split())
    result.append(a+b)
    count += 1
for i in range(x):
    print('Case #', end='')
    print(i+1, end=': ')
    print(result[i])
