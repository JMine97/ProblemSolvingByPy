'''
비어있는 칸 중에서 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 자리를 정한다.
1을 만족하는 칸이 여러 개이면, 인접한 칸 중에서 비어있는 칸이 가장 많은 칸으로 자리를 정한다.
2를 만족하는 칸도 여러 개인 경우에는 행의 번호가 가장 작은 칸으로, 그러한 칸도 여러 개이면 열의 번호가 가장 작은 칸으로 자리를 정한다.

만족도는 자리 배치가 모두 끝난 후에 구할 수 있음
0-0, 1-1, 2-10, 3-100, 4-1000
'''

N=int(input())
place=[[0]*N for _ in range(N)]
move=[[-1, 0],[0, -1],[1, 0],[0, 1]]

like={}
for _ in range(N**2):
    a=list(map(int, input().split()))
    st=a[0]
    like[st]=a[1:]

    max_like=-1
    max_empty=-1
    max_r=0
    max_c=0
    for r in range(N):
        for c in range(N):
            if place[r][c]==0:
                #탐색
                like_cnt=0
                empty_cnt=0

                for dr, dc in move:
                    nr, nc=r+dr, c+dc
                    if 0 <= nr < N and 0 <= nc < N:
                        if place[nr][nc] in like[st]:
                            like_cnt+=1
                        if place[nr][nc] ==0:
                            empty_cnt+=1

                if max_like<like_cnt or (max_like==like_cnt and max_empty<empty_cnt):
                    max_like=like_cnt
                    max_empty=empty_cnt
                    max_r=r
                    max_c=c
    place[max_r][max_c]=st

happy=0
for r in range(N):
    for c in range(N):
        st=place[r][c]
        like_cnt=0
        for dr, dc in move:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N:
                if place[nr][nc] in like[st]:
                    like_cnt += 1
        if like_cnt!=0:
            happy+=10**(like_cnt-1)

#만족도
print(happy)