'''
투포인터
'''

n, s = map(int, input().split())
arr=list(map(int, input().split()))

##현재 합이 s 미만이면 end++, 이상이면 start++
##end-start<ret 이면 ret 갱신

start=0; end=0
inf=float('inf')
sumv=0; ret=float('inf') #양의 무한대를 나타냄

for start in range(n):
    while sumv<s and end<n:
        sumv+=arr[end]
        end+=1

    if sumv>=s:
        ret = min(ret, end - start)

    sumv-=arr[start]

if ret==inf:
    print(0)

else:
    print(ret)