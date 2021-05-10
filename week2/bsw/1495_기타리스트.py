
#개수N 시작볼륨S 최대볼륨M
N, S, M = 3, 5, 10
V = [5, 3, 7]


from collections import deque

q=[S]

for v in V:
    tmp = []
    for q_ in q:
        if q_ + v <= M:
            tmp.append(q_+v)
        if q_ - v >= 0:
            tmp.append(q_-v)
    q=tmp


print(q)