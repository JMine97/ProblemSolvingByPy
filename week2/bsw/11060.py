
def sol():
    N = int(input())
    arr = list(map(int, input().split()))
    DP = [-1]*N
    DP[0] = 0


    for i in range(N):
        for j in range(1, arr[i]+1):
            if i+j >= N:
                break
            elif DP[i] == -1:
                break
            if DP[i+j] != -1:
                DP[i+j] = min(DP[i]+1, DP[i+j])
            else:
                DP[i+j] = DP[i]+1

    print(DP[N-1])
    print(DP)


sol()

