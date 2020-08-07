a = input()
result = []
for i in range(len(a)) :
    if a[i].isupper():
        if 65 <= ord(a[i]) <= 77:
            result.append(chr(ord(a[i])+ 13))
        else :
            result.append(chr(ord(a[i]) - 13))


    elif a[i].islower():
        if 97 <= ord(a[i]) <= 109:
            result.append(chr(ord(a[i]) + 13))
        else:
            result.append(chr(ord(a[i]) - 13))

    else :
        result.append(a[i])

for i in result:
    print(i, end='')
            

