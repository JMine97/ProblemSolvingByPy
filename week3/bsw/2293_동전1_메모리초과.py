# 2293 동전1 메모리초과
n, k = map(int, input().split())
coin = []
for _ in range(n):
    coin.append(int(input()))

cnt=[[0]*(k+1) for _ in range(n)]
for i in range(k+1):
    if i % coin[0] == 0:
        cnt[0][i] = 1
    else:
        cnt[0][i] = 0


for i in range(1, n):
    for j in range(k+1):
        if coin[i] > j:
            cnt[i][j] = cnt[i-1][j]
        elif coin[i] == j:
            cnt[i][j] = cnt[i-1][j] + 1
        else:
            cnt[i][j] = cnt[i-1][j] + cnt[i][j-coin[i]]


print(cnt[n-1][k])


'''k
C   0   1   2   3   4   5   6   7   8   9   10
1   1   1   1   1   1   1   1   1   1   1   1
2   1   1   2   2   3   3   4   4   5   5   6
5   1   1   2   2   3   4   5   6   7   8   10

coin(i) = i번째 동전의 가치
cnt(i, k) = i번째 동전까지 사용해서 k를 만드는 경우의 수

coin(i) > k # cnt(i, k) = cnt(i-1, k)
coin(i) = k # cnt(i, k) = cnt(i-1, k) + 1
coin(i) < k # cnt(i, k) = cnt(i-1, k) + cnt(i, k - coin(i))

'''