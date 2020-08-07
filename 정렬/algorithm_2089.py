num = int(input())
result = []

if num ==0 : print(0)
else:

    while num:
        if num%(-2):
            result.append(1)
            num = num // (-2) +1

        else:
            result.append(0)
            num //= -2

for i in range(len(result)-1,-1,-1):
    print(result[i],end='')
