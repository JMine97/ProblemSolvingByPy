#한 박스에 맥주 20개
# 50미터에 한 병 씩
from collections import deque

t=int(input())


#맨허튼 거리
#페스티벌 o happy
#페스티벌 x sad
for _ in range(t):
    n=int(input()) #편의점의 개수

    home=list(map(int, input().split()))
    store_fes=deque()
    for _ in range(n+1):
        store_fes.append(list(map(int, input().split())))

    flag=False
    q=deque()
    q.append(home)
    visited=[home]
    while q:
        r, c = q.popleft()

        if r==store_fes[-1][0] and c==store_fes[-1][1]:
            flag=True; break

        for i, j in store_fes:
            if [i, j] not in visited:
                dist=abs(r-i)+abs(c-j)
                if dist<=50*20:
                    visited.append([i, j])
                    q.append([i, j])

    if flag:
        print("happy")
    else:
        print("sad")
