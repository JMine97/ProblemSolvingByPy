#2003 수들의 합 2
# idx 두개를 움직이는 문제 ==> "while()"
# 항상 반복문에서 0번째 index를 어떻게 처리할 것인가를 생각

# index 처리 미완성

N, M = map(int, input().split())
arr = list(map(int, input().split()))

cnt = 0
Sum = 0

left=0
right=0
while(left<N):
    if right == N:
        break
    elif Sum < M:
        Sum += arr[right]
        right+=1    
    elif Sum > M:
        Sum -= arr[left]
        left+=1
    elif Sum == M:
        cnt += 1
        Sum += arr[right]

    if left > right:
        if left < N and right < N:
            Sum = 0
            right = left
    

print(cnt)




'''
Sum에 j를 i+1부터 1씩 증가하면서 더해주면서 M과 비교
Sum > M :: Sum - arr[i] 
            i++
Sum == M :: Cnt++
            i=j+1
Sum < M :: i=j+1




'''

