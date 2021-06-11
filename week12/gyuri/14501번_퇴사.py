#14501번_퇴사
'''
최대이익을 내는 상담을 해야한다
1<=N<=15, 상담할 수 있는 일수
DP, 공간을 만들어 준다
'''
import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * 21 # dp[N] = N일 까지 얻는 이익
sch = []
for i in range(n):
    sch.append(list(map(int, input().split())))
    # dp[i] = sch[i][1]

for i in range(n):
    # 전날의 보상이 더 클 경우  
    if dp[i] > dp[i+1]:
        dp[i+1] = dp[i]
    # 기존 x날의 보상보다 i 날에 일해서 받는 보상이 더 클 경우 
    if dp[i+sch[i][0]] < dp[i] + sch[i][1]:
        dp[i+sch[i][0]] = dp[i] + sch[i][1]

print(dp[n])
