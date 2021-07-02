# LCA 알고리즘 (Lowest Common Ancestor)
# 푼 방식 : 1. 노드의 부모를 각각 값에 넣는다. 2. 루트에서 자신까지 내려오기까지 저장해 2개의 큐를 비교하면서 일치하지 않을 때를 리턴한다. 
from collections import deque

t = int(input())

for _ in range(t):
  
  n = int(input())
  graph = [0 for _ in range(n+1)] # root는 0이 됨. 
  
  for i in range(n-1): # 간선 개수(n-1) - 1
    a, b = map(int, input().split())
    graph[b] = a # b의 부모는 a
    
  x, y = map(int, input().split())

  x_parents = []
  i = x
  while i:
      x_parents.append(i)
      i = graph[i]

  j = y
  while j:
      if j in x_parents:
          break
      j = graph[j]

  print(j)
