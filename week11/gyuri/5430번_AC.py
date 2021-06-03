# 5430번_AC.py
'''
정수 배열에 연산을 하기 위해 만든 언어
두 가지 함수
- R 함수 : 배열에 있는 숫자의 순서를 뒤집는 함수
- D 함수 : 첫 번째 숫자를 버리는 함수, 빈배열일 경우 에러 발생
ex) RDD [1,2,3,4] -> 4,3,2,1 -> 3,2,1 -> 2,1
ex2) RRD [1,1,2,3,5,8] ->
r이 몇개 쌓이고 d가 들어오는지에 따라 함수 수행
'''
import sys
from collections import deque
input = sys.stdin.readline

answer = []
t = int(input())

for _ in range(t):
    p = input().rstrip('\n')
    n = int(input())
    x_list = input().rstrip('\n')
    if (x_list) != '[]':
        x_list = deque(list(map(str, x_list.lstrip('[').rstrip(']').split(','))))
        flag = 1
        for i in p:
            if i == "R":
                flag *= (-1)
            elif i == "D":
                if x_list:
                    if flag == 1:
                        x_list.popleft()
                    else:
                        x_list.pop()
                else:
                    print('error')
                    break
        if x_list:
            if flag != 1:
                x_list.reverse()
            x_list = list(x_list)
            print('[', end="")
            print(','.join(x_list), end='')
            print(']')
    else :
        print('error')
