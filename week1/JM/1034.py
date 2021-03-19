import sys
input=sys.stdin.readline

n, m=map(int, input().split())
arr=[input().rstrip() for _ in range(n)]
k=int(input())
# print(arr)
cnt=[0]*n

for i in range(n):
    zero_cnt = arr[i].count('0')
    if zero_cnt%2==k%2 and zero_cnt<=k:
        for j in range(n):
            if arr[i]==arr[j]:
                cnt[i]+=1

print(max(cnt))

'''''''''''
1. 0의 개수와 k가 일치하는 행 탐색
2. 그 중 초기상태가 가장 많이 동일한 것의 갯수 반환
2. 한 열을 여러번 누를 수 있음을 주의하기
'''''''''''