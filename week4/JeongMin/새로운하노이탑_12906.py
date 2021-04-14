# set, dict는 내부적으로 hash를 이용해 자료를 저장하기 때문에 in 시간복잡도가 avg O(1)
# list, tupple은 avg O(n)이라고 합니다
# index가 필요하지 않은 자료구조일 때 set 쓰는 것 추천

import sys
from collections import deque

input = sys.stdin.readline

arr = []
for _ in range(3):
    c = input()
    if c[0]=='0':
        arr.append('')
    else:
        a, b = c.split()
        arr.append(b)

q = deque()
q.append([arr[0], arr[1], arr[2], 0])  # A막대, B막대, C막대, cnt
visited = set()  # 이미 방문한 형태면 루프 계속 돌려도 어차피 같은 형태가 append 될테니까 뺌

while q:
    a, b, c, cnt = q.popleft()
    if a.count('A') == len(a) and b.count('B') == len(b) and c.count('C') == len(c):
        # 탈출 조건 #A에는 A만 있고, B에는 B만 있고, C에는 C만 있을 때
        print(cnt)
        break
    if (a, b, c) not in visited:
        visited.add((a, b, c))

        if len(a) > 0:
            q.append([a[:-1], b + a[-1], c, cnt + 1])
            q.append([a[:-1], b, c + a[-1], cnt + 1])
        if len(b) > 0:
            q.append([a + b[-1], b[:-1], c, cnt + 1])
            q.append([a, b[:-1], c + b[-1], cnt + 1])
        if len(c) > 0:
            q.append([a + c[-1], b, c[:-1], cnt + 1])
            q.append([a, b + c[-1], c[:-1], cnt + 1])
