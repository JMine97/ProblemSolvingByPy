n, m = map(int, input().split())
lst = list(map(int, input().split()))

def solution():
    count = 0
    start,end = 0,1
    summ = lst[start]

    while start < n:
         #합이 딱 m이면 
        if summ == m:
            summ -= lst[start] 
            count += 1 #정답 횟수 +1
            start += 1 #start를 늘려서 값을 줄임
            
        if end == n and summ < m:
            break

        #합이 m보다 작으면
        elif summ < m:
            summ += lst[end]
            end += 1 #end를 늘려서 값을 늘림

        #합이 m보다 크면 start를 늘려서 값을 줄임 
        elif summ > m :
            summ -= lst[start]
            start += 1
    

    return count

print(solution())
