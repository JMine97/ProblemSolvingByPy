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
'''
i = 0
dp[0] vs dp[0 + 1] -> 아직 다 0이니깐 pass
dp[0 +sch[0][0]] vs dp[0] + sch[0][1] -> 원래 그 자리에 있던 dp 값과 i날 일해서 받은 보상 중 큰 값으로 update 
[0,0,0,10,0,0,0,...]

i = 1
[0, 0, 0, 10, 0, 0, 20, 0,...]

i = 2
[0, 0, 0, 10, 0, 0, 20, 0,...]

i = 3
if dp[3] > dp[3+1]
이때 dp[3]은 i =1 일한거로 10이라는 보상을 받았다.
dp[3] > dp[3+1] , 10 > 0
[0, 0, 0, 10, 30, 0, 20, 0,...]

즉, 첫번째 if 문을 통해서 전날 값으로 시작하게끔하여 최대수익이 가능하게 한다. 누적?
'''
