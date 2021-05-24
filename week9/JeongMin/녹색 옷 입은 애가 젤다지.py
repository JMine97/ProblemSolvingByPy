import sys
import heapq as hp
input=sys.stdin.readline
INF=10**9

i=1
while True:
    n=int(input()) #동굴의 크기
    if n==0:
        break

    cave=[]
    for _ in range(n):
        cave.append(list(map(int, input().split())))

    #[0][0]에서 시작
    #상하좌우
    #[n-1][n-1]까지 이동
    #도둑 루피에 의해 잃을 수밖에 없는 최소금액

    q=[]
    hp.heappush(q, (cave[0][0], 0, 0)) #현재 잃은 금액, 탐색할 row, col
    distance=[[INF]*n for _ in range(n)] #최소 금액 담음
    while q:
        money, row, col = hp.heappop(q)
        if money>distance[row][col] or row>=n-1 and col>=n-1:
            continue

        #탐색할 가치가 있는 노드
        for dr, dc in [-1, 0], [1, 0], [0, 1], [0, -1]:
            nr=row+dr
            nc=col+dc
            if 0<=nr<n and 0<=nc<n:
                if money+cave[nr][nc]<distance[nr][nc]:
                    hp.heappush(q, (money+cave[nr][nc], nr, nc))
                    distance[nr][nc]=money+cave[nr][nc]

    print('Problem %d: %d' % (i+1,distance[n-1][n-1]))
    i+=1
