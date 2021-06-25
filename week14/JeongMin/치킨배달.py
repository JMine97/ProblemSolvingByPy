#0 빈칸, 1 집, 2 치킨집
from itertools import combinations

n, m = map(int, input().split())
graph=[]
home=[]
chicken=[]
for _ in range(n):
    graph.append(list(map(int, input().split())))

#치킨집과 집의 좌표 받음
for r in range(n):
    for c in range(n):
        if graph[r][c]==1:
            home.append([r, c])
        elif graph[r][c]==2:
            chicken.append([r, c])

def dist():
    ret=0
    for h in home:
        tmp=10**8
        home_r, home_c = h[0], h[1]
        for com in comb_chicken:
            chi_r, chi_c = com[0], com[1]
            tmp=min(tmp, abs(home_r-chi_r)+abs(home_c-chi_c))
        ret+=tmp
    return ret

ret=10**8
for comb_chicken in combinations(chicken, m):
    ret = min(ret, dist())
print(ret)
