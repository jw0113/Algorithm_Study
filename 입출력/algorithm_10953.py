num = int(input())
count=0
result=[]
while count < num:
    a,b= map(int, input().split(','))
    if 0<a<10 and 0<b<10:
        result.append(a+b)
        count+=1
        
for i in range(len(result)):     
    print(result[i])
