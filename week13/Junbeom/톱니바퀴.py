# # idea : 시계방향으로 흐르면 popleft 후 append, 반시계방향으로 흐르면 pop 후 appendleft

import sys
from collections import deque
input = sys.stdin.readline

li = []
for _ in range(4):
    li.append(deque(input().rstrip()))


k = int(input())
command = [] # num, dir 
for i in range(k):
    command.append(list(map(int, input().split())))

# 왼쪽 톱니바퀴 확인 
def rotate_left(num, dir): 
    if num < 0: # 왼쪽 끝까지 간 경우 
        return 
    if li[num][2] != li[num+1][6]:
        rotate_left(num-1, -dir)   
        li[num].rotate(dir)

#오른쪽 톱니바퀴 확인
def rotate_right(num, dir): 
    if num > 3: # 오른쪽 끝까지 간 경우 
        return
    if li[num][6] != li[num-1][2]:
        rotate_right(num+1, -dir)
        li[num].rotate(dir)

for i in range(k):
    num = command[i][0] - 1
    dir = command[i][1]
    
    rotate_left(num-1, -dir) # 인접한 바퀴는 해당 바퀴랑 반대방향을 돌아야함. 함수 안에서 돌아야하는지 아닌지를 판단. 
    rotate_right(num+1, -dir)
    # 기존의 톱니바퀴를 회전시키는 작업 
    li[num].rotate(dir)

answer = 0

if li[0][0] == '1':
    answer += 1
if li[1][0] == '1':
    answer += 2
if li[2][0] == '1':
    answer += 4
if li[3][0] == '1':
    answer += 8
    
print(answer)

