num = int(input())
a = list(map(int, input().split()))
dp = list(0 for i in range(num))
dp1 = list(0 for i in range(num))

for i in range(num):
    dpmax = 0
    if i==0 : dp[i] = 1
    else:
        for j in range(i):
            if a[i] > a[j] and dpmax < dp[j] :
                dpmax = dp[j]

        dp[i] = dpmax + 1

for i in range(num-1, -1, -1):
    dpmax = 0
    if i==0: dp1[i] = 1
    else:
        for j in range(num-1, i, -1):
            if a[i] > a[j] and dpmax < dp1[j]:
                dpmax = dp1[j]

        dp1[i] = dpmax + 1

print(max((dp[i]+dp1[i])-1 for i in range(num)))
