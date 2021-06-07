import sys
input = sys.stdin.readline

t = int(input())
    
for _ in range(t):
    answer = 'YES'
    n = int(input())

    phone = [input().strip('\n') for _ in range(n)]

    d = {}
    for p in phone:
        d[p] = 1
    #print(d)
    for p in phone:
        comp = ''
        for s in p:
            comp+=s
            if comp in d.keys() and comp != p:
                answer = 'NO'

    print(answer)
            
