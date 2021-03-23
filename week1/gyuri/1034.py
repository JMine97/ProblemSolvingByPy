# 정민님 코드 참고해서 수정 
N, M = map(int, input().split())
table = []                      # 전체 테이블
cnt = [0] * N
answer = 0
for i in range(N):
    table.append(list(map(int, input())))
# arr=[input().rstrip() for _ in range(n)] 을 통해서 간편하게
# print(arr) 결과 : ['10','01'] 형태
K = int(input())

# 모든 행을 확인해서 K 횟수 안에 그 행의 모든 램프를 통일시키는 것이 가능한지 check
for i in range(N):
    table_cnt = table[i].count(0)
    if table_cnt % 2 == K % 2 and table_cnt <= K :
        for j in range(N):
            # table안 행의 초기 형태가 같으면, k번의 조작 후에도 같을 거니깐
            if table[i] == table[j]:
                cnt[i]+=1
print(max(cnt))



# 틀렸습니다 
N, M = map(int, input().split())

table = []                      # 전체 테이블
col = [0 for _ in range(M)]     # 각 열별 꺼진 램프 개수
answer = 0
for i in range(N):
    table.append(list(map(int, input())))

K = int(input())
while K > 0:
    # 각 열마다 꺼진 램프 개수
    for i in range(N):
        for j in range(M):
            col[j] = 1 + col[j] if table[i][j] == 0 else col[j]
    max_idx = col.index(max(col))
    for i in range(N):
        table[i][max_idx] = 1 if table[i][max_idx] == 0 else 0
    K = K - 1
for i in range(N):
    if 0 not in table[i]:
        answer += 1
print(answer)
