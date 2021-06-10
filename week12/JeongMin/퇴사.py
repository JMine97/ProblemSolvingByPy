n=int(input())
t=[] #[3, 5, 1, 1, 2, 4, 2]
p=[] #[10, 20, 10, 20, 15, 40, 200]
dp=[0]*(n+1) #현재 날짜를 기준으로 나올 수 있는 최댓값

for _ in range(n):
    a, b = map(int, input().split())
    t.append(a); p.append(b)

for i in range(n-1, -1, -1):
    if n>=t[i]+i:
        dp[i]=max(dp[i+1], p[i]+dp[i+t[i]])
    else:
        dp[i] = dp[i+1]
print(dp[0])
