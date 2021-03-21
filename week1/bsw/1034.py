
N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
K = int(input())


ans =0
for n in range(N):
    sameCol = 0
    if arr[n].count('0') <= K and arr[n].count('0')%2 == K%2:
        for i in range(N):
            if arr[n] == arr[i]:
                sameCol += 1
                ans = max(ans, sameCol)
            

print(ans)

        
# 0 1 1 0
# 1 0 0 0
# 0 1 0 0
# 1 0 1 1 
# 0 0 0 0 

'''''''''''''''''''''''
1. 행의 모든 숫자가 같아야 동시에 정답이 될 수 있다
2. 각 행의 0의 갯수와 K가 동시에 홀수이거나 짝수여야 한다
3. 1과 2를 모두 만족하는 행의 최대 갯수를 출력
'''''''''''''''''''''''
