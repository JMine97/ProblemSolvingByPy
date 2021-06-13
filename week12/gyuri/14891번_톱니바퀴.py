# 서로 맞닿은 톱니의 극이 다르다면, B는 A가 회전한 방향과 반대방향으로 회전
# 서로 맞닿은 톱니의 극이 같으면, 회전하지 않는다.
# 12시방향부터, 시계방향 순서대로 N극은 0, S극은 1로 나타나있다.
# deque의 rotate 함수
# 이문제의 핵심은...? 구현?

import sys
from collections import deque
input = sys.stdin.readline
deq = deque()
for i in range(4):
    deq.append(deque(input().rstrip()))

def function(idx, turn, dir):
    # S, N극 check
    if dir == 'L':
        if idx < 3:
            if deq[idx][2] != deq[idx + 1][6]:
                function(idx + 1, turn * (-1), 'L')
                deq[idx + 1].rotate(turn)
        else:
            return
    else:
        if 0 < idx :
            if deq[idx][6] != deq[idx-1][2]:
                function(idx-1, turn * (-1), 'R')
                deq[idx-1].rotate(turn)
        else:
            return

k = int(input())
for i in range(k):
    a, b = map(int, input().split())
    if b == 1:
        # 시계방향
        function(a-1, -1, 'R')
        function(a-1, -1, 'L')
        deq[a-1].rotate(1)
    else:
        # 반시계방향
        function(a-1, 1, 'R')
        function(a-1, 1, 'L')
        deq[a-1].rotate(-1)
answer = 0
for i in range(4):
    if int(deq[i][0]):
        answer += (2**i)

print(answer)
