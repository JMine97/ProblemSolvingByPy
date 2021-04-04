# 나눗셈은 정수 나눗셈으로 몫만 취함. 
# 음수을 양수로 나눌 때는 C++14의 기준을 따름. 

def dfs(i, res, add, sub, mul, div):
  global max_result, min_result
  if i == n-1: # 연산자를 다 사용했으면
    max_result = max(res, max_result)
    min_result = min(res, min_result)
    return

  else:
    if add:
      dfs(i+1, res+li[i+1], add-1, sub, mul, div)
    if sub:
      dfs(i+1, res-li[i+1], add, sub-1, mul, div)
    if mul:
      dfs(i+1, res*li[i+1], add, sub, mul-1, div)
    if div: # div
      dfs(i+1, int(res/li[i+1]), add, sub, mul, div-1) # C++ 14 기준을 따지려면 //을 쓰면 안 됨. 

n = int(input())

li = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

max_result = -1000000001
min_result = 1000000001

dfs(0, li[0], add, sub, mul, div)

print(max_result)
print(min_result)
