# 투포인터 알고리즘 
import sys
INF = int(1e9)
input = sys.stdin.readline 
n, s = map(int, input().split())
li = list(map(int, input().split()))

left, right = 0, 0 # two pointer
summ = 0
length = INF # answer 

while True:
    if summ >= s: # s보다 크면
        length = min(length, right-left) # length 갱신
        summ -= li[left] # left 이동하기 위해 미리 제거 
        left += 1 # 한칸 이동 

    elif right == n: # 탈출조건. 전체 탐색이 끝나면 
        break
    
    else: # s보다 작은 상황 
        summ += li[right]
        right += 1

if length == INF:
    print(0)
else : 
    print(length)

