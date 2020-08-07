num = int(input())
maxdict = {}

for i in range(num):
    n = int(input())
    if n in maxdict :
        maxdict[n] += 1
    else:
        maxdict[n] = 1

maxdict = sorted(maxdict.items(), key= lambda x: (-x[1],x[0]))
print(maxdict[0][0])
