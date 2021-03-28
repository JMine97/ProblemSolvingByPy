n,s,m = map(int, input().split()) #곡개수 n, 시작 볼륨s, 최대볼륨 m
v = list(map(int, input().split())) #줄 수 있는 볼륨의 차이

dp = [[False]*(m +1) for _ in range(n+1)] #dp[i][j]는 i번째 노래에서 j볼륨으로 연주 가능한 지 여부 판단
dp[0][s] = True #0번째 노래일 때 s의 크기 볼륨으로 연주가 가능하다

for i in range(1, n+1): #노래 각각에 대하여
    for j in range(0, m+1): #이 볼륨으로 연주 가능한 지 판단
        if dp[i-1][j] == 0: 
            continue

        if j-v[i-1] >= 0: #볼륨을 줄였을 때 볼륨이 0을 넘으면
            dp[i][j-v[i-1]] = True #i번째 노래에서 작아진 볼륨으로 연주가능

        if j + v[i-1] <= m: #볼륨을 키웠을 때 최대 볼륨을 넘지 않으면
            dp[i][j+v[i-1]] = True #커진 볼륨으로 연주 가능

result = -1
for i in range(m,-1,-1): #최고 볼륨부터 하나씩 내리면서
    if dp[n][i] == True: #마지막곡에서 그 볼륨에서 연주가 가능하면
        result = i #그 볼륨을 최고 볼륨으로 설정
        break
    
print(result)
            
            
    


        
