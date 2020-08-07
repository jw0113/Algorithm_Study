n,k = map(int, input().split())
while True:
    inList = list(map(int, input().split()))
    if len(inList) != n: break
    inList = sorted(inList)

    print(inList[k-1])
    break
