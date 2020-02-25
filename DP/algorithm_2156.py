num = int(input())
dp = [0]
dp1 = [0]

for i in range(num):
    dp.append(int(input()))
    
dp1.append(dp[1])

if num>1:
    dp1.append(dp[1]+dp[2])
    
if num>2:
    for i in range(3,num+1):
        dp1.append(max(dp1[i-1], dp1[i-2]+dp[i], dp1[i-3]+dp[i-1]+dp[i]))

print(dp1[num])
