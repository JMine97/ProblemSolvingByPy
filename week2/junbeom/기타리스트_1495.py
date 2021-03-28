# BFS로 접근하면 쉬움.
# 그러나 DP로 푸는 것이 맞는 듯 -> 왜냐하면 2초, 그리고 적은 메모리 초과.
# 그러나 메모리가 너무 작다. 128은 bfs 하다가 메모리 초과가 나기 쉬움.  -> 역시 BFS로 푸니까 메모리 초과가 남. 

# idea
# 1. 전형적인 탐색 문제로 파악이 되지만 메모리가 128MB 밖에 되지 않기 때문에 BFS를 사용하는 방법 말고, DFS나 DP를 생각해야 한다.
# 2. 시간이 넉넉하므로 위험하게 탐색으로 시도하지 않고, 안전하게 DP로 진행한다. 
# 3. BFS로 풀었을 시 메모리 초과 발생. 

import sys
from collections import deque

n, s, m = map(int, input().split())
li = list(map(int, input().split()))

dp = [[0] * (m+1) for _ in range(n+1)]  # dp[n][s] : n번째 곡일 때, s 볼륨이 가능한 여부 

dp[0][s] = True # 시작은 True.

for i in range(1, n+1):
  for j in range(0, m+1): # 인덱스 주의. 
    if dp[i-1][j] == False: # 볼륨이 사용 불가능하면 Continue 
      continue
    if j-li[i-1] >= 0: 
      dp[i][j - li[i-1]] = True 
    if j+li[i-1] <= m:
      dp[i][j + li[i-1]] = True


last = (dp[-1]) 
ans = -1
for idx in range(len(last)):
  if last[idx] == True: # 인덱스 중 가장 큰 것을 뺌. -> 마지막 곡 볼륨 중 최댓값
    ans = max(idx, ans)

print(ans)
  
# BFS 풀이. 메모리 초과