n = int(input())
lst = list(map(int, input().split()))

dp = [-1] * n

def bfs(start):
    q = []
    q.append(start)
    dp[start] = 0
    
    while q:
        now = q.pop(0)
        jump = lst[now]
        for i in range(jump, 0, -1):
            if now + i < n and dp[now + i] == -1:
                dp[now + i] = dp[now] + 1
                q.append(now + i)

bfs(0)
print(dp[-1])


"""
#문제 이해 잘못해서 이렇게 풀었다가 틀려서 답보고 위에 방식으로 풀었는데 완벽히 이해는 못했습니다.
n = int(input())
lst = list(map(int, input().split()))

def solution(curr_index):
    count = 0
    next_index = 0

    if(lst[curr_index] == 0):
        print(0)
        return
    
    while True :  
        curr_index = next_index
        max_jump = lst[curr_index] #최대로 점프할 수 있는  칸 수

        if curr_index + max_jump >= n-1:
            count += 1
            print(count)
            return

        for jump in range(max_jump,0,-1): #한칸 씩 줄여가면서
            #print("무한")
            if curr_index + jump > n-1 : #범위를 벗어나면 
                count += 1
                print(count)
                return

            else: #점프한 게 범위를 벗어 나지 않으면
                count += 1 #점프함
                next_index = curr_index + jump 
                break
            
                
        if lst[curr_index] == 0 and curr_index < n - 1: #현재 칸에서 점프할 수 없으면
            #print(lst[curr_index], " ", curr_index)
            print(-1)
            return -1
        
        
solution(0)
"""
