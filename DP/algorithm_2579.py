num = int(input())
a = []
dp = [0 for i in range(num)]

for i in range(num):
    a.append(int(input()))

dp[0] = a[0]
dp[1] = a[0] + a[1]
dp[2] = max(a[0]+a[2], a[1]+a[2])

for i in range(3, num):
    dp[i] = max(dp[i-2]+a[i], dp[i-3]+a[i]+a[i-1])

print(dp[num-1])
