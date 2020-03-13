num = int(input())
dp = [0 for i in range(num+1)]
dp[2] = 3

for i in range(4,num+1,2):
            
    dp[i] += dp[2]*dp[i-2]
            
    for j in range(4,i,2):
                
        dp[i] += dp[i-j]*2
        
    dp[i] += 2

print(dp[num])
