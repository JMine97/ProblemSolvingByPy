#15787번_기차가 어둠을 헤치고 은하수를.py
'''
N개의 기차
기차는 20개의 좌석
명령 1.
    1 i x : i번째 기차, x 좌석에 사람을 태워라
명령 2.
    2 i x : i번째 기차, x 좌석에 앉은 사람은 하차
명령 3.
    3 i : i번째 기차에 앉은 모든 승객 뒤로 한칸. 20번 좌석 사람은 하차
명령 4.
    4 i : i번째 기차 모두 앞으로 한칸. 1번 좌석은 하차
기차가 지나갈 때 승객이 앉은 상태를 목록에 기록하며
이미 목록에 존재하는 기록이라면 해당 기차는 은하수를 건널수 없다.

기록이 존재하기 때문에 set으로 check해서 은하수를 건널 수 있는지 check
'''
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
trains = [set([]) for _ in range(n)]

for _ in range(m):
    op = list(map(int, input().split()))
    if op[0] == 1:
        trains[op[1]-1].add(op[2])
    if op[0] == 2:
        trains[op[1] - 1].discard(op[2])
    if op[0] == 3:
        tr = list(trains[op[1] - 1])
        temp = set()
        for t in tr:
            if t + 1 > 20:
                continue
            temp.add(t+1)
        trains[op[1] - 1] = temp
    if op[0] == 4:
        tr = list(trains[op[1] - 1])
        temp = set()
        for t in tr:
            if t - 1 < 1 :
                continue
            temp.add(t - 1)
        trains[op[1] - 1] = temp
answer = set()
for train in trains:
    t = tuple(sorted(train))
    answer.add(t)
print(len(answer))

------------------------------------------------------
import  sys
from collections import deque
input = sys.stdin.readline
n, m = map(int,input().split())
train = [deque([0]*20) for _ in range(n)]
for _ in range(m):
    box=list(map(int,input().split()))
    if box[0]==1:
        train[box[1]-1][box[2]-1]=1
    elif box[0]==2:
        train[box[1]-1][box[2]-1]=0
    elif box[0]==3:
        train[box[1]-1].rotate(1)
        train[box[1]-1][0]=0
    else:
        train[box[1]-1].rotate(-1)
        train[box[1]-1][19]=0
answer=[]
for i in train:
    if i not in answer:
        answer.append(i)
print(len(answer))
