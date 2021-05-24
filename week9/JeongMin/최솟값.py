import sys
from math import *
input = sys.stdin.readline
INF = int(1e9)
# 최소값이 최상단 루트 노드에 있는 tree 생성

def init(node, s, e): #루트노드
    if s == e:
        tree[node] = num_list[s]
        return tree[node]
    mid = (s+e) // 2
    tree[node] = min(init(node*2, s, mid), init(node*2+1, mid+1, e))
    return tree[node]

# 내가 찾으려는 범위 [l, r]
# 처음 탐색시작할 노드 번호 node
# 그 노드가 커버하는 인덱스 범위 s, e
# left, right 사이에 현재 노드의 커버범위가 들어온다.
# 후보로 선정한다.
# left, right 와 현재 노드의 커버범위가 전혀 겹치지 않는다.
# 버린다.
# 애매하게 걸친다.
# 더 깊이 들어가서 조사한다.
def min_function(node, s, e, l, r):
    print(node, s, e, l, r)

    #범위 이탈
    if r < s or e < l:
        return INF
    # min을 구하는 거니깐 l이 s 범위안에 존재하기 때문에 더이상 재귀하지 않고 return
    # ??????
    # 각 노드가 담당하는 범위 ⊂ 탐색범위
    if l <= s and e <= r:
        return tree[node]

    # 각 노드가 담당하는 범위 ⊃ 탐색 범위
    mid = (s+e) // 2
    return min(min_function(node*2, s, mid, l, r), min_function(node*2+1, mid+1, e, l, r))

answer = []
n, m = map(int, input().split()) #입력 갯수, 구간
# list의 높이를 구하고 올림.
h = int(ceil(log2(n)))+1
# 1 을 왼쪽으로 h + 1 번 이동. 즉 2 ** h
t_size = 2 ** h
tree = [0] * t_size
num_list = []
for _ in range(n):
    num_list.append(int(input()))

init(1, 0, n-1)
print(tree)
for _ in range(m):
    a, b = map(int, input().split())
    answer.append(min_function(1,0,n-1,a-1,b-1))

# for i in answer:
#     print(i)