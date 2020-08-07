t = int(input())
a = 0
input_list = [0,]

def dfs(start, input_lists, result):
    result += [start]
    if input_lists[start] not in result:
        result = dfs(input_lists[start], input_lists, result)


while a<t:
    n = int(input())
    input_list.extend(list(map(int, input().split())))

    

    
