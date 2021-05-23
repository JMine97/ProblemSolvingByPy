#2042번_구간 합 구하기.py
'''
어떤 N개의 수가 주어져 있다.
그런데 중간에 수의 변경이 빈번히 일어나고 그
중간에 어떤 부분의 합을 구하려 한다
# n = n개의 수 m = 수의 변경 횟수, k = 구간의 합,
'''
import sys
input = sys.stdin.readline
answer = []
n, m, k = map(int, input().split()) # n = n개의 수 m = 수의 변경 횟수, k = 구간의 합,
num_list = [int(input()) for _ in range(n)]
tree = [0] * (n*4)

def init(s, e, node):
    if s == e :
        tree[node] = num_list[s]
        return tree[node]
    mid = (s + e) // 2
    tree[node] = init(s, mid, node * 2) + init(mid + 1, e, node * 2 + 1)
    return tree[node]

def update(s, e, node, idx, diff):
    #if not (s <= idx <= e):
    if idx < s or idx > e:
        return
    tree[node] += diff
    if s == e :
        num_list[s] += diff
        return
    mid = (s + e) // 2
    update(s, mid, node*2, idx, diff)
    update(mid+1, e, node*2+1, idx, diff)

def sum_function(s, e, node, left, right):
    # 범위 밖에 있는 경우
    if left > e or right < s:
        return 0
    # 범위 안에 있는 경우
    if left <= s and e <= right:
        return tree[node]
    mid = (s + e) // 2
    return sum_function(s, mid, node*2, left, right) + sum_function(mid+1, e, node*2+1, left, right)

init(0, n-1, 1)

for i in range(k+m):
    a, b, c = map(int, input().split())
    # a = 1
    if a == 1:
        # b번째 수를 c로 바꾸고
        update(0, n - 1, 1, b-1, c - num_list[b-1])
    elif a == 2:
        # a가 2인 경우에는 b번째 수부터 c 번째 수까지의 합을 구하여출력
        answer.append(sum_function(0, n - 1, 1, b-1, c-1))
for a in answer:
    print(a)


