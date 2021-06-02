'''
R : 뒤집기
D : popleft

'''
from collections import deque

T = int(input())
ans=[]
for _ in range(T):
    
    error = 0
    func = input()
    arr_len = int(input())
    if arr_len == 0:
        arr = deque(input())
        arr.clear()
    else:
        arr = deque(input().strip('[]').split(','))
    

    # while 'RR' in func:
    #     func = func.replace('RR', '')

    flag=1
    try:
        for f in func:
            if f == "R":
                flag *= -1
            elif f == "D":
                if flag == 1:
                    arr.popleft()
                elif flag == -1:
                    arr.pop()
    except:
        print('error')
        continue

    #print(func)
    if flag == -1:
        arr.reverse()
    print('['+','.join(arr)+']')
    



    