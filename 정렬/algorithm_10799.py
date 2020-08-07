a = list(input())
stack = []
result = 0
for i in range(len(a)):
    if a[i] == '(':
        stack.append(a[i])
    else:
        stack.pop()
        if a[i-1] == '(':
            result += len(stack)
        else:
            result += 1

print(result)
        
        
