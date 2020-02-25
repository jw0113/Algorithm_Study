num = int(input())
input_list = list(map(int,input().split()))

dp = list(0 for i in range(num))
dp[0] = input_list[0]

for i in range(1,num):
    result = []
    for j in range(i):
        if input_list[i] > input_list[j]:
            result.append(dp[j])

    if result :
        #dp[i] = dp[input_list.index(max(result))]+input_list[i]
        dp[i] = max(result) + input_list[i]
    else:
        dp[i] = input_list[i]
        
print(max(dp))
