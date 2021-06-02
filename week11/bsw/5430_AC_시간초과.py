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
    

    while 'RR' in func:
        func = func.replace('RR', '')

    try:
        for f in func:
            if f == "R":
                arr.reverse()
            elif f == "D":
                arr.popleft()
    except:
        print('error')
        continue

    #print(func)
    print('['+','.join(arr)+']')

    



    