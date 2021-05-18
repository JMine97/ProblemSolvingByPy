from collections import deque
from sys import stdin
input = stdin.readline

def bfs():
    q = deque()
    q.append(a)
    dist[a] = 0
    
    while q:
        x = q.popleft()
        if x == b: #치환 완료했으면 이때까지 최소 횟수 반환
            return dist[x]
        
        for nx in v[x]: 
            if dist[nx] == -1: 
                q.append(nx) 
                dist[nx] = dist[x]+1 
    return -1

a, b = map(int, input().split()) # a를 b로 바꾸려고 함
n, m = map(int, input().split()) # 전체 문자의 수 n 치환 가능한 문자쌍의 수 m
v = [[] for _ in range(n+1)] 
dist = [-1]*(n+1)

for i in range(m): 
    x, y = map(int, input().split()) #치환 가능한 문자쌍
    v[x].append(y) 
    v[y].append(x)

print(bfs())


