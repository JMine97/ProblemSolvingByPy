'''
펜윅트리 사용
'''

import sys
input=sys.stdin.readline

n, m, k = map(int, input().split())

arr=[0]*(n+1)
tree=[0]*(n+1)

#i번째 수까지의 누적 합 계산
def prefix_sum(i):
    result=0
    while i>0:
        result+=tree[i]
        i-=(i&-i)
    return result

#i번째 수를 dif만큼 더함
#그에 영향을 받는 수들도 더함
def update(i, dif):
    while i<=n:
        tree[i]+=dif
        i+=(i&-i)

#start부터 end까지의 구간 합
def interval_sum(start, end):
    return prefix_sum(end)-prefix_sum(start-1)

for i in range(1, n+1):
    x=int(input())
    arr[i]=x
    update(i, x)

for i in range(m+k):
    a, b, c = map(int, input().split())
    if a==1:
        update(b, c - arr[b])
        arr[b]=c
    else:
        print(interval_sum(b, c))