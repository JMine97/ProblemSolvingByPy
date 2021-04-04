#2293 동전1
#리스트 두개 고정
n, k = map(int, input().split())
coin = []
for _ in range(n):
    coin.append(int(input()))

cnt=[[0]*(k+1) for _ in range(2)] # *2는 왜?

for i in range(k+1):
    if i % coin[0] == 0:
        cnt[0][i] = 1
    else:
        cnt[0][i] = 0


for i in range(n):
    cnt[0] = cnt[1]
    cnt[1] = [0]*(k+1)

    for j in range(k+1):
        if coin[i] > j:
            cnt[1][j] = cnt[0][j]
        elif coin[i] == j:
            cnt[1][j] = cnt[0][j] + 1
        else:
            cnt[1][j] = cnt[0][j] + cnt[1][j-coin[i]]
        
    
print(cnt[1][k])


'''k
C   0   1   2   3   4   5   6   7   8   9   10
1   1   1   1   1   1   1   1   1   1   1   1
2   1   1   2   2   3   3   4   4   5   5   6
5   1   1   2   2   3   4   5   6   7   8   10
'''