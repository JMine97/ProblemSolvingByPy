# 연산자 끼워넣기
# N개의 수로 이루어진 수열 , N-1개의 연산자 ( +, -, * / 4가지)
# 수의 순서 변경 불가능
# 연산자의 우선 순위를 무시
# 나눗셈은 몫만
# c++14의 기준으로 음수를 양수로 나눈다.(양수로 바꾼뒤 몫을 취하고, 그 몫을 음수로 바꾼 것과 같다)

# 식의 결과 최대값 & 최소값을 구해라

# 1.입력 : N <= 11
# 2.입력 : N개의 수 <=100
# 3. 입력 : 연산자의 개수

# 풀이 방법
# 동적할당? 그리디? 완전 탐색?
# 경우의 수를 모두 구한다?
# DFS

# 연산자의 개수가 너무많으면?

# 스택? 재귀?

# 연산자를 재귀로 넣어보자
# 각 숫자 ver로 op_cnt가 필요할 것 같은데

import sys

input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
op = list(map(int, input().split()))

max_num = -1000000001
min_num = 1000000001
def op_func(i, result, plus,sub, multi, div):
    global max_num
    global min_num
    i+=1
    if i == n:
        max_num = max(max_num, result)
        min_num = min(min_num, result)
        return
    if plus < op[0]:
        op_func(i, a[i] + result, plus+1,sub, multi, div)
    if sub < op[1]:
        op_func(i, result - a[i], plus,sub+1, multi, div)
    if multi < op[2]:
        op_func(i, a[i] * result, plus,sub, multi+1, div)
    if div < op[3]:
        if result <= 0:
            result = abs(result) // a[i]
            result *= (-1)
            op_func(i, result, plus, sub, multi, div + 1)
        else:
            op_func(i, result//a[i], plus,sub, multi, div+1)

if op[0] != 0:
    op_func(1, a[0] + a[1], 1, 0, 0, 0)
if op[1] != 0:
    op_func(1, a[0] - a[1], 0, 1, 0, 0)
if op[2] != 0:
    op_func(1, a[0] * a[1], 0, 0, 1, 0)
if op[3] != 0:
    op_func(1, a[0] // a[1], 0, 0, 0, 1)
print(max_num)
print(min_num)

'''
[풀이 설명 및 더 좋은 풀이 제공]
- 풀이 설명
숫자의 순서는 바뀌지 않고 연산자만 변경된다.
그래서 모든 경우의 수를 확인하기 위해서 재귀를 통해서 푼다.
각 식마다 개별적인 연산자 사용 횟수를 가지고 있어야한다. 
DFS?라고 한다 

-더 좋은 풀이 
재귀를 넘길 때 초기값을 연산자가 있는 리스트를 넘겨주면서 연산자를 사용할 때 마다 -1을 하면 풀이가 더 깔끔하다. 
'''
