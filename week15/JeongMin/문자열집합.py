'''
import sys 쓰기 전 : 928ms
            쓴 후 : 168ms
차이 꽤 많이 나는 듯
'''

from collections import defaultdict
import sys
input=sys.stdin.readline

n, m = map(int, input().split())
s=defaultdict(int)
for _ in range(n):
    s[input().strip()]

ret=0
for _ in range(m):
    if input().strip() in s:
        ret+=1

print(ret)