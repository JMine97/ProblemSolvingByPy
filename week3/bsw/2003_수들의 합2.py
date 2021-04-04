#2003 수들의 합 2
# idx 두개를 움직이는 문제 ==> "while()"
# 항상 반복문에서 0번째 index를 어떻게 처리할 것인가를 생각

N, M = map(int, input().split())
arr = list(map(int, input().split()))

cnt = 0
Sum = 0

i=0
j=0
while(i<N and j<N):
    
    if Sum < M:
        Sum += arr[j]
        j+=1    
    elif Sum > M:
        Sum -= arr[i]
        i+=1
    elif Sum == M:
        cnt += 1
        i+=1
        j=i
        Sum = 0

    if i>j:
        Sum = 0
        j=i
    


print(cnt)




'''
Sum에 j를 i+1부터 1씩 증가하면서 더해주면서 M과 비교
Sum > M :: Sum - arr[i] 
            i++
Sum == M :: Cnt++
            i=j+1
Sum < M :: i=j+1




'''

