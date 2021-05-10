# 메모리초과
# 개수N 시작볼륨S 최대볼륨M
N, S, M = 3, 5, 10
V = [5, 3, 7]

N, S, M = map(int, input().split())
V = list(map(int, input().split()))

q=[S]
for v in V:
    tmp = []
    if not q:
        q = [-1]
        break
    for q_ in q:
        if q_ + v <= M:
            tmp.append(q_+v)
        if q_ - v >= 0:
            tmp.append(q_-v)
    q=[t for t in tmp]


print(max(q))