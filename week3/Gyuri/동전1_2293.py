# 2293번 동전1

# n가지 종류의 동전 = k 합 의 경우의 수
# 순서만 다른 것은 같은 경우

# 1차 시도 : stack? 형태 -> 메모리 초과
import sys
input = sys.stdin.readline
n, k = map(int, input().split())
c = [int(input()) for _ in range(n)]
dp = [0 for i in range(k + 1)]
dp[0] = 1

for i in c:
    for j in range(i, k + 1):
      #print(j , i)
      dp[j] += dp[j - i]
      #print(dp)
print(dp[k])
