x = int(input())
count = 0
while count < x:
    a,b = map(int, input().split())
    if 0<a<10 and 0<b<10 :
        print('Case #', end='')
        print(count+1, end=': ')
        print(a,b,sep=' + ',end=' = ')
        print(a+b)
        count += 1
