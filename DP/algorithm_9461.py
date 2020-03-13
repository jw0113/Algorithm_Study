count = int(input())
dp = [0,1,1]

for c in range(count) :
    num = int(input())

    for i in range(len(dp),num+1):
        dp.append(dp[i-3] + dp[i-2])

    print(dp[num])    
