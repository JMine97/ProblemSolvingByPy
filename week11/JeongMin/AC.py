import sys
from collections import deque
input=sys.stdin.readline

'''
R 뒤집기
D 처음 두 숫자 버리기

deque는 인덱스 슬라이싱이 안 된다
'''
for _ in range(int(input())):
    p=input().strip()
    n=int(input())

    arr=input().strip('[]\n').rsplit(',')

    if arr[0]=='':
        q=deque()
    else:
        q=deque(arr)

    start=0

    flag=1
    try:
        for pp in p:
            if pp=='R':
                flag*=-1
            elif pp=='D':
                if flag==1:
                    q.popleft()
                else:
                    q.pop()
    except:
        print('error')
        continue


    q=list(q)
    print('[', end='')
    if flag==1:
        print(','.join(q), end='')
    else:
        print(','.join(q[::-1]), end='')
    print(']')
