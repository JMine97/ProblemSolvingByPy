N, M = map(int, input().split())

S = {}
for _ in range(N):
    S[input()] = 1

check = [input() for _ in range(M)]


ans=0
for chk in check:
    if chk in S:
        ans+=1

print(ans)