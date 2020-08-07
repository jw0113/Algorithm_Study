def gcd(a,b):
    while b > 0:
        tmp = a%b
        a = b
        b = tmp
    return a

for i in range(int(input())):
    sum = 0
    num = list(map(int, input().split()))

    for j in range(1, len(num)-1):
        for z in range(j+1, len(num)):
            sum += gcd(num[j], num[z])

    print(sum)

    
