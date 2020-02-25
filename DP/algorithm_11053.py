num = int(input())
dp = list(map(int,input().split()))

m = list(0 for i in range(num))

for i in range(num):
    for j in range(i):
        if dp[i] > dp[j] and m[i] < m[j]:
            m[i] = m[j]
    m[i] += 1

print(max(m))
