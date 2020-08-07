a = input()
result = [-1] * 26

for i in range(len(a)):
    if result[ord(a[i])-97] < 0 : result[ord(a[i])-97] = i

for i in result:
    print(i, end=' ')
