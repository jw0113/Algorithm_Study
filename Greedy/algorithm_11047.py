n,k = map(int, input().split())

input_list = []
for i in range(n) :
    input_list.append(int(input()))

count = 0
for j in range(n-1,-1,-1):
    if input_list[j] <= k :
        count += k//input_list[j]
        k %= input_list[j]

print(count)
