num = int(input())
a = list(map(int, input().split()))
dp = [0 for i in range(num)]

for i in range(num-1,-1,-1):

    if i == (num-1):
        dp[i] = 1

    else:
        dpmax = 0
        for j in range(num-1, -1, -1):
            
            if a[j] < a[i] and dpmax < dp[j]:
                dpmax = dp[j]
                
        dp[i] = dpmax +1

print(max(dp))

