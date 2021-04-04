# 시간 제한 0.5초 -> 짧은 시간 제한을 고려하고 문제 풀이에 임해야 함. 

import sys
from collections import deque

n, m = map(int, input().split())
li = list(map(int, input().split()))


count = 0
for i in range(len(li)): # i - 왼쪽 인덱스, j - 오른쪽 인덱스
  temp = 0
  if li[i] == m: # i 하나로 m인 경우  
    count += 1
    continue 
  temp += li[i]
  for j in range(i+1, len(li)): # j는 오른쪽 인덱스 . 하나씩 늘려주면서 Count를 따져 줌. 
    temp += li[j]
    if temp == m:
      count += 1
      break
    elif temp > m:
      break
    
print(count)

