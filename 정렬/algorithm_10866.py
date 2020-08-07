import sys

num = int(input())
result = []
for i in range(num):
    a = sys.stdin.readline().split()

    if a[0] == 'push_front':
        result.insert(0,a[1])

    elif a[0] == 'push_back':
        result.append(a[1])

    elif a[0] == 'pop_front':
        if len(result) == 0 : print(-1)
        else:
            print(result.pop(0))

    elif a[0] == 'pop_back':
        if len(result) == 0 : print(-1)
        else :
            print(result.pop())

    elif a[0] == 'size':
        print(len(result))

    elif a[0] == 'empty' :
        if len(result) == 0 : print(1)
        else : print(0)

    elif a[0] == 'front':
        if len(result) == 0 : print(-1)
        else : print(result[0])

    elif a[0] == 'back' :
        if len(result) == 0 : print(-1)
        else : print(result[-1])
