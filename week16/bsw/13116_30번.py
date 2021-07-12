import sys
input = sys.stdin.readline
# input이 5만개라 readline 쓰는게 효율적일듯

T = int(input())

tree = {}

for i in range(1, 1024):
    tree[i] = i//2

#print(tree)
for _ in range(T):
    a, b = map(int, input().split())
    answer = 0

    ans_a = set()
    ans_b = set()

    while a in tree:
        ans_a.add(a)
        a = tree[a]

    while b in tree:
        ans_b.add(b)
        b = tree[b]

    print(max(ans_a & ans_b)*10)
    
