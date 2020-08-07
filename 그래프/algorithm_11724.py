import sys
sys.setrecursionlimit(10000)

n, m = map(int, sys.stdin.readline().split())
a = [[] for _ in range(n+1)]
check = [False]*(n+1)
for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    a[u].append(v)
    a[v].append(u)

def dfs(now):
    check[now] = True
    for i in a[now]:
        if check[i] is False:
            dfs(i)

cnt = 0
for i in range(1, n+1):
    if check[i] is False:
        dfs(i)
        cnt += 1
print(cnt)
