num = int(input())
a = list(map(int, input().split()))

if len(a) == num :
    count = 0
    for i in range(len(a)) :
        re = 0
        if a[i]==1 : continue
        else:
            for j in range(1, a[i]+1):
                if a[i]%j == 0: re+=1
            if re == 2: count+=1


    print(count)
    
    

