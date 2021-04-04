#계속 고쳐도 시간초과인데 어떻게 고쳐야 할지 모르겠습니다
from collections import deque

n, m = map(int, input().split())
move = {}

for i in range(n+m):
    location, m = map(int, input().split())
    move[location] = m
    visited = [False]*101
    

def solution():
    q = deque([(1,0)])
    count = 0
    visited[1] = True
    
    while q:
            node, count = q.popleft()

                   
        #1~6까지 더해봄
            for i in range(1,7):
                nx = node+i
                
                if nx == 100:
                    return count+1
                
                if nx > 100:
                    continue
                    
                #사다리나 뱀을 만나면 움직임
                if nx in move.keys():
                    nx = move[nx]

                if nx not in visited:
                    visited[nx] = True
                    q.append((nx, count+1))
                    
                                  
    return count
        
        
    
print(solution())

