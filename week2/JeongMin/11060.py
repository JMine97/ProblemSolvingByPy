import sys
input=sys.stdin.readline

n=int(input())
a=list(map(int, input().split()))
dp=[1000]*n

dp[0]=0
cnt=0
# dp에 점프 수를 담는다
for i in range(n):
    jump=a[i] #점프 할 수 있는 칸 수
    if jump==0: #점프 못하면 다음으로
        continue
    if i+1+jump>n: #최대 칸수 넘으면 최대 칸수로
        jump_loc=n
    else:
        jump_loc=i+1+jump
    for j in range(i+1, jump_loc): #점프로 갈 수 있는 칸들
        dp[j]=min(dp[i]+1, dp[j])

if dp[-1]!=1000:
    print(dp[-1])
else:
    print(-1)
