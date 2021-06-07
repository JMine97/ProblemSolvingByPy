# 9357번_패션왕 신해빈.py
'''
dictionary,
복잡도 : O(n*m)?
'''
import sys
input = sys.stdin.readline

def function(n):
    m = int(input())
    answer = 1
    total = 0
    d = {}
    if n == 0:
        print(0)
        return
    for _ in range(m):
        name, kind = input().split()
        if kind in d.keys():
            d[kind] += 1
        else:
            d[kind] = 1
    for i in d.values():
        answer *= (i+1)
    print(answer - 1)
n = int(input())
for _ in range(n):
    function(n)
