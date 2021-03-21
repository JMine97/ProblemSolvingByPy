


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
