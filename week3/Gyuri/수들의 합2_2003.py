# 2003 수들의 합2

# N개의 수로 된 수열a
# a[i] ~ a[j]까지의 합 = M 이 되는 경우의 수

# 1. 그냥 탐색 -> 시간초과
# 2. 깊이우선탐색
# 더블 포인터 -> 언제쓰는거더라?, 합이 작아질때?

# 입력
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
li = list(map(int, input().split()))
s = 0
e = 1
cnt = 0
# 종료 조건이 뭐지?
while s < n and e <= n:
  if sum(li[s:e]) == m:
    #print(s, e)
    cnt+=1
    s+=1
    e+=1
  elif sum(li[s:e]) > m:
    s+=1
  elif sum(li[s:e]) < m:
    e+=1

print(cnt)

# 두 포인터(1차원 배열에서 두개의 포인터)
# 두포인터 사용 조건: 배열의 원소가 자연수
# end pointer 증가 -> 부분합 증가
# start pointer 증가 -> 부분합 감소
