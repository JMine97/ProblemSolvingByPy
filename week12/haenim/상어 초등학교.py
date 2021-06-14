"""

좋아하는 학생이 주위에 많도록 자리를 정하자

<조건>
1. 비어있는 칸 중에서 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 자리를 정한다.
2. 1을 만족하는 칸이 여러 개이면, 인접한 칸 중에서 비어있는 칸이 가장 많은 칸으로 자리를 정한다.
3. 2를 만족하는 칸도 여러 개인 경우에는 행의 번호가 가장 작은 칸으로, 그러한 칸도 여러 개이면
    열의 번호가 가장 작은 칸으로 자리를 정한다.

만족도의 총 합을 출력하는 문제

만족도는 그 학생과 인접한 칸에 앉은 좋아하는 학생 수로 구함
0이면 0, 1이면 1, 2면 10, 3이면 100, 4면 1000


=> 그냥 하라는 대로 풀면 됨

O(n^3)

"""

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

N = int(input()) 

seat_lst = [[0]*N for _ in range(N)] # 학생 자리 정할 배열
like = dict() # 좋아하는 학생 저장 
result = 0
 
for _ in range(N*N): #학생 수 만큼 반복
    input_list = list(map(int, input().split())) # 학생번호와 그 학생이 좋아하는 학생 4명을 입력으로 받음(4 2 5 1 7)
    like[input_list[0]] = input_list[1:] # { 학생 번호(4) : 학생이 좋아하는 학생들(2 5 1 7) }  
    
    max_x = 0 
    max_y = 0
    max_like = -1
    max_empty = -1
    
    for i in range(N): 
        for j in range(N):
            if seat_lst[i][j] == 0: #이 좌석에 학생이 없으면 이 자리에서
                likecnt = 0 
                emptycnt = 0
                
                for k in range(4): # 상하좌우로 움직임
                    nx = i + dx[k]
                    ny = j + dy[k]
                    
                    if 0 <= nx < N and 0 <= ny < N: # 범위 내에 있으면
                        
                        if seat_lst[nx][ny] in input_list: #이 자리에 좋아하는 학생이 있으면
                            likecnt += 1 #like 수를 하나 올림 
                            
                        if seat_lst[nx][ny] == 0: # 비어 있는 칸이면
                            emptycnt += 1 # 비어있는 칸 수를 하나 늘림
                            
                if max_like < likecnt or (max_like == likecnt and max_empty < emptycnt):
                    # 주위에 좋아하는 학생이 많거나 좋아하는 학생 수가 같다면 자리 주위에 빈 자리가 많으면
                    # 그 자리를 저장
                    max_x = i 
                    max_y = j
                    max_like = likecnt
                    max_empty = emptycnt
                    
    seat_lst[max_x][max_y] = input_list[0] # 자리 배정

# 만족도 계산
for i in range(N): 
    for j in range(N):
        cnt = 0
        liked_student = like[seat_lst[i][j]] #i,j번째에 앉은 학생이 좋아하는 학생들 리스트
        
        for k in range(4): # 상하좌우로 움직이면서
            nx = i + dx[k]
            ny = j + dy[k]
            
            if 0 <= nx < N and 0 <= ny < N:
                if seat_lst[nx][ny] in liked_student: # 좋아하는 학생이 주위에 있으면
                    cnt += 1 # 증가
                    
        if cnt != 0:
            result += 10 ** (cnt-1) #좋아하는 학생 수 토대로 만족도 계산
            
print(result)
