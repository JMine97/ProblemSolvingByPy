n, m = map(int, input().split())
lst = list(map(int, input().split()))

#부분 합이 m이 되는 경우의 수 구하기
# 투 포인터 알고리즘
# 1 1 1 1 에서 합이 2 되는 경우의 수 찾기
#   s   e

def solution():
    count = 0
    start,end = 0,1
    summ = lst[start] #부분합

    while start < n:
         #합이 딱 m이면 
        if summ == m:
            start += 1 #start를 늘려서 값을 줄임
            summ -= lst[start] 
            count += 1 #정답 횟수 +1
            
            
        if end == n and summ < m:
            break

        #합이 m보다 작으면
        elif summ < m:
            end += 1 #end를 늘려서 값을 늘림
            summ += lst[end]

        #합이 m보다 크면 start를 늘려서 값을 줄임 
        elif summ > m :
            start += 1
            summ -= lst[start]
            
    

    return count

print(solution())

# dp 많이 안나온다
# 탐색 위주!! 개마니나옴 dfs bfs 완전탐색 그래프 탐색
# 이진탐색나오면 좀 어려워짐
# bfs dfs 시간초과나면 백트래킹
# 구현 - 좀 더 어렵다

# dp
# 문제를 푸는 방식이 dp가 많은건가 dp문제는 대회문제에 많이 쓰인다 코테에서는 마니안쓰임
# 10%정도 나온다
# 탐색에서 dp 메모제이션같은 테크닉
# 점화식을 세워서 들어감,, 만드는 게 어렵다,, 규칙찾기,,

#람다의 조은기능,,
#회의실 / 강의실 배정 
