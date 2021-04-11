#12906 새로운 하노이 탑

# 원판이 이동할 때마다 하노이 탑의 현재 상태를 저장해 재사용 해야 한다
# DP로 접근 -> 실패 -> BFS로 접근해야 한다
# 
# 큐에 무엇을 담을 것인가???
# -> 현재 하노이 탑의 상태 
#                   + 이동 횟수 (전역 변수로 관리를 시도했으나 실패)
#
#
# 최소값을 구하는 문제와 최소 횟수를 구하는 문제는 다르다
# 최소값을 구하는 경우 -> min 함수 사용
# 최소 횟수 -> 원하는 조건을 만족했을 경우 break
# 
#
# ☆ 중간 element의 추가, 제거, 비교 연산의 경우
# list -> O(N)
# set/tuple -> O(1)
#
# 순서가 중요하지 않은 자료구조가 필요할 경우 리스트 사용을 자제하는 것이 좋아보임


from collections import deque

cnt = []
stage = []

for _ in range(3):
    try:
        c, s = input().split()
        cnt.append(int(c))
        stage.append(s)
    except:
        cnt.append(0)
        stage.append("")

q = deque()
visited = set()

# 현재 상태를 저장
q.append((stage[0], stage[1], stage[2], 0))

while q:
    A, B, C, count = q.popleft()

    # 모든 원판이 올바르게 배치된 경우 종료
    if A.count('A')==len(A) and B.count('B')==len(B) and C.count('C')==len(C):
        print(count)
        break

    if (A, B, C) not in visited:
        visited.add((A, B, C))
        
        # A 막대에 원판이 있을 경우
        if len(A) > 0:
            # A -> B
            q.append((A[0:-1], B + A[-1], C, count+1))
            # A -> C
            q.append((A[0:-1], B, C + A[-1], count+1))
        
        # B 막대에 원판이 있을 경우
        if len(B) > 0:
            # B -> A
            q.append((A + B[-1], B[0:-1], C, count+1))
            # B -> C
            q.append((A, B[0:-1], C + B[-1], count+1))

        # C 막대에 원판이 있을 경우
        if len(C) > 0:
            # C -> A
            q.append((A + C[-1], B, C[0:-1], count+1))
            # C -> B
            q.append((A, B + C[-1], C[0:-1], count+1))
            

