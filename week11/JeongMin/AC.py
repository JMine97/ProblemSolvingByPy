import sys
from collections import deque
input=sys.stdin.readline

'''
R 뒤집기
D 처음 두 숫자 버리기
'''
for _ in range(int(input())):
    p=input().strip()
    n=int(input())

    arr=input().strip().lstrip('[').rstrip(']').split(',')

    if arr[0]=='':
        q=deque()
    else:
        q=deque(arr)

    start=0

    Flag=False
    for pp in p:
        if pp=='R':
            if start==0:
                start=len(q)-1
            else:
                start=0
        elif pp=='D':
            if len(q) == 0:
                Flag = not Flag
                print("error")
                break

            if start==0:
                q.popleft()
            else:
                q.pop()

    if not Flag:
        q=list(q)
        print('[', end='')
        if start==0:
            print(','.join(q), end='')
        else:
            print(','.join(q[::-1]), end='')
        print(']')
