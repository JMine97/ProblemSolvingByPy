'''
 12시방향부터 시계방향 순서대로 주어진다. 
 N극은 0, S극은 1
'''
from collections import deque
wheel = []
for _ in range(4):
    lane = input()
    tmp = deque()
    for l in lane:
        tmp.append(l)
    wheel.append(tmp)

N = int(input())
print(wheel)

def rotation(num, d):
    if d == 1:
        wheel[num].appendleft(wheel[num].pop())
    elif d == -1:
        wheel[num].append(wheel[num].popleft())

def check_right(n, r):
    if 4 <= n+1:
        return
    if wheel[n][2] != wheel[n+1][6]:
        r[n+1] = -r[n]
        check_right(n+1, r)

def check_left(n, r):
    if n-1 < 0:
        return
    if wheel[n-1][2] != wheel[n][6]:
        r[n-1] = -r[n]
        check_left(n-1, r)

for _ in range(N):
    num, direct = map(int, input().split())
    num-=1 # idx = 톱니번호 - 1

    rotate = [0]*4
    rotate[num] = direct
    
    check_right(num, rotate)
    check_left(num, rotate)

    for i in range(4):
        rotation(i, rotate[i])

answer = 0
for i in range(4):
    if wheel[i][0] == '1':
        answer+= 2**i

print(answer)