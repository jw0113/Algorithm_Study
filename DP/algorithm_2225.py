n,k = map(int, input().split())
dp = [[0 for j in range(n+1)] for i in range(k)]
for i in range(n+1):
    dp[0][i] = 1

for i in range(1,k):
    for j in range(n+1):
        for z in range(j+1):
            dp[i][j] += dp[i-1][z]

print(dp[k-1][n]%1000000000)
