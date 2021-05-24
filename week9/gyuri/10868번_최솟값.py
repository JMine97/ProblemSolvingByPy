#10868번_최솟값.py
'''
N개의 정수,
(a, b)쌍이 M개
(1, 3) -> 1번, 2번, 3번 정수 중에서 최솟값
'''
import sys
from math import *
input = sys.stdin.readline
INF = int(1e9)
# 최소값이 최상단 루트 노드에 있는 tree 생성

def init(node, s, e):
    if s == e:
        tree[node] = num_list[s]
        return tree[node]
    mid = (s+e) // 2
    tree[node] = min(init(node*2, s, mid), init(node*2+1, mid+1, e))
    return tree[node]


def min_function(node, s, e, l, r):
    if r < s or e < l:
        return INF
    # min을 구하는 거니깐 l이 s 범위안에 존재하기 때문에 더이상 재귀하지 않고 return
    # ??????
    if l <= s and e <= r:
        return tree[node]
    mid = (s+e) // 2
    return min(min_function(node*2, s, mid, l, r), min_function(node*2+1, mid+1, e, l, r))

answer = []
n, m = map(int, input().split())
# list의 높이를 구하고 올림.
h = int(ceil(log2(n)))
# n_size = 2 ** (h+1)
# 1 을 왼쪽으로 h + 1 번 이동. 즉 2 ** h+1
t_size = 1 << (h+1)
tree = [0] * t_size
num_list = []
for _ in range(n):
    num_list.append(int(input()))

init(1, 0, n-1)

for _ in range(m):
    a, b = map(int, input().split())
    answer.append(min_function(1,0,n-1,a-1,b-1))

for i in answer:
    print(i)
