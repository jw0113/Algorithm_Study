num1, num2 = map(int, input().split())
for i in range(num1, num2+1):
    count=0
    for j in range(2,int((i**0.5)+1)):
        if i%j == 0: count +=1
    if count ==0: print(i)

