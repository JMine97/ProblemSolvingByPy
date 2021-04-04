# dfs해서 올바른 dfs 순서인지만 비교하려고 했는데 동일 라인에 있는 노드를 교체하는 작업이 필요
# 다 찾아서 한 이중배열에 담아 입력받은 리스트가 있는 지 판단하지 말고, 입력받은 리스트로 우선순위를 받아 탐색이 가능한 건지 역으로 풀 것. 

n = int(input())

graph = [[] for _ in range(n+1)] # 상호 저장하기 위해서 

for _ in range(n-1): # 간선의 개수 = 노드의 개수 - 1
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

li = list(map(int, input().split()))
visited = [False]*(n+1) # dfs에서 방문처리 
order = [-1]*(n+1) 

li_dfs = [] # 올바른지 아닌지 비교하기 위한 완성 리스트 

for i in range(1, n+1): # 입력받은 리스트로 인해, 우선순위를 변경하기 위한 order라는 리스트 생성
  order[li[i-1]] = i

for i in range(1, n+1): # order 에 맞는 순서대로 다시 그래프 노드 순서를 바꿈. 
  graph[i] = sorted(graph[i], key= lambda x : order[x])

def dfs(graph, v, visited): # dfs 
  visited[v] = True
  li_dfs.append(v)

  for i in graph[v]:
    if not visited[i]:  # 방문을 하지 않은 곳만 dfs 
      dfs(graph, i, visited)

dfs(graph, 1, visited)

if li == li_dfs:
  print(1)
else:
  print(0)

