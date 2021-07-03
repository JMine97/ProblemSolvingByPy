import sys
input = sys.stdin.readline

n, m = map(int, input().split())

dic = {}
for _ in range(n):
    s = str(input())
    dic[s] = 0

count = 0
for _ in range(m):
    s = str(input())
    if s in dic:
        count += 1

print(count)
