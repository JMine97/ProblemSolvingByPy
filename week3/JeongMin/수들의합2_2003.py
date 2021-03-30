import sys
input=sys.stdin.readline

n, m = map(int, input().split())
a=list(map(int, input().split()))

cnt=0
start=0
sum=0
for end in range(n):
    sum += a[end]
    if sum == m:
        cnt += 1
    elif sum < m:
        continue
    elif sum>m:
        while start<=end:
            sum-=a[start]
            start+=1
            if sum==m:
                cnt+=1
                break
            elif sum<m:
                break
print(cnt)

''''''''''''''''''''''
이렇게 하면 될 것 같아서 그냥 풀었는데
이게 슬라이딩 윈도우 알고리즘이라고 하네요
'''''''''''''''''''''''

