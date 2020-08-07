import sys

num = int(input())
result = []
for i in range(num):
    a = sys.stdin.readline().split()

    if a[0] == 'push':
        result.append(int(a[1]))

    elif a[0] == 'pop':
        if not result: print(-1)
        else: print(result.pop())

    elif a[0] == 'size': print(len(result))

    elif a[0] == 'empty':
        if not result : print(1)
        else : print(0)

    elif a[0] == 'top' :
        if not result: print(-1)
        else: print(result[-1])
    
