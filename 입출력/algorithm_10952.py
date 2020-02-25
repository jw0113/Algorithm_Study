result=[]
while True:
    a,b= map(int, input().split())
    if a==0 and b==0 : break
    else :
        if 0<a<10 and 0<b<10:
            result.append(a+b)
for i in range(len(result)):     
    print(result[i])
