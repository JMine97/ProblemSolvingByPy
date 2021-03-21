N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
K = int(input())


ans =0
for n in range(N):
    sameCol = 0
    #print(arr[n].count('0'))
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

# 2
# 3
# 3
# 1
# 4

'''''''''''''''''''''''


'''''''''''''''''''''''