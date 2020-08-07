num = int(input())
for i in range(num):
    c = 0
    a = list(input())

    for j in a:
        if c == 0 and j == ')':
            c -= 1
            break

        elif j == '(':
            c += 1

        elif j == ')':
            c -= 1

    if c == 0 : print('YES')
    else : print('NO')
