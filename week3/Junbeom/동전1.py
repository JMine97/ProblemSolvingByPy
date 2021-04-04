# DP (memoziation)

n, k = map(int, input().split())
li = []
dp = [0]*(k+1)

dp[0] = 1 # 

for _ in range(n):
  li.append(int(input()))

for i in li:
  for j in range(i, k+1):
    dp[j] += dp[j-i]

print(dp[k])


