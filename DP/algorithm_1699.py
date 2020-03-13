num = int(input())
dp = [0 for i in range(num+1)]
#제곱근 넣음
d = [i*i for i in range(1, 317)]

for i in range(1, num+1):
    result = []
    for j in d:
        
        if j > i:
            break
        
        result.append(dp[i - j])
    dp[i] = min(result) + 1
    
print(dp[num])
    
