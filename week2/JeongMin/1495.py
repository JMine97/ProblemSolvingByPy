import sys
input = sys.stdin.readline

n, s, m = map(int, input().split())
v = list(map(int, input().split()))
dp = [[0]*(m+1) for _ in range(n+1)]
v=[0]+v #dp와 v인덱스 같게

# dp에 가능한 볼륨은 1처리
dp[0][s]=1
for i in range(1, len(dp)): #곡 돌음
    for j in range(len(dp[0])): #볼륨 돌음
        if dp[i-1][j]==1:
            if m>=j+v[i]:
                dp[i][j+v[i]]=1
            if j-v[i]>=0:
                dp[i][j-v[i]]=1
# print(dp)
result=-1
for i in range(m,-1,-1):
    if dp[-1][i]==1:
        result=i
        break
print(result)
