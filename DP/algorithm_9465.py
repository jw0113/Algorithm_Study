num = int(input())

for z in range(num):
    m = []
    
    col = int(input())
    for i in range(2):
        m.append(list(map(int,input().split())))

    m[0][1] += m[1][0]
    m[1][1] += m[0][0]

    for i in range(2,col):
        m[0][i] += max(m[1][i-1], m[1][i-2])
        m[1][i] += max(m[0][i-1], m[0][i-2])

    print(max(m[0][col-1], m[1][col-1]))
