
'''
N이 2의 거듭제곱일 경우 항상 1개가 될 수 있다
==> 물병의 갯수를 추가하다보면 반드시 정답이 존재하게 됨

1 1 1 1 1
2 2 1
4 1

5
2 ... 1
1 ... 0
0 ... 1


1. N//2가 0이 될 때 까지 cnt += N%2 반복
2. 0이 되는순간의 cnt의 합이 K보다 클 경우 N+1 해준뒤 1번 반복
3. cnt < K 일 경우 cnt 출력

nlogn -> 시간초과
'''


N, K = map(int, input().split())
#i=0
def loop(N):
    cnt=0
    #global i
    while N:
        cnt += N%2
        N //= 2
        #i+=1
    return cnt

ans=0
while 1:
    cnt = loop(N+ans)
    if cnt <= K:
        break
    else:
        ans+=1
print(ans)

