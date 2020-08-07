import sys
while True:
    try:
        result = [0,0,0,0]
        a = input()

        for i in a:
            if i.isupper() : result[1] += 1
            elif i.islower() : result[0] += 1
            elif i.isdigit() : result[2] += 1
            elif i.isspace() : result[3] += 1

        for i in range(len(result)):
            print(result[i],end=' ')
        print('')

    except EOFError:
        break
        
    
