n, m, k = map(int,input().split())

team = 0
while n>=2 and m>0  :
    n -= 2
    m -= 1
    if n+m >= k : 
        team += 1

print(team)