n,m,v = map(int, input().split())
mx = [[0] * (n+1) for i in range(n+1)]
for i in range(m):
    a,b = map(int, input().split())
    mx[a][b] = 1
    mx[b][a] = 1

def dfs(start, matrix, result):
    result += [start]
    for i in range(len(matrix[start])):
        if matrix[start][i] == 1 and i not in result:
            result  = dfs(i,matrix, result)

    return result

print(*dfs(v,mx,[]))
        
    
