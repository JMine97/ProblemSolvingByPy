import sys
from itertools import combinations

'''
a, n, t, i, c 는 무조건 배우고 나머지 알파벳 중 무엇을 배워야
가장 많은 단어를 읽을 수 있는지

set()을 활용해 보자!
1. set()은 문자열로 넣어도 원소 하나하나로 접근한다는 점
2. combination에 현재 list 길이보다 큰 값이 들어오면 combination 함수가 돌아가지 않는다는 점
3. set() 연산 : |= 합집합, - 차집합
'''

input = sys.stdin.readline
n, k = map(int, input().split())

k -= 5
if k < 0:
    print(0)
else:
    word, bits, basecom = [], [], set()
    bit = {chr(ord('a') + i): 1 << i for i in range(26)}
    baseword = set('antic')

    for _ in range(n):
        word = set(input().strip()) - baseword  # 빼기
        basecom |= word  # 더하기
        tmp = 0
        for w in word:
            tmp += bit[w]
        bits.append(tmp)

    # bits, com
    ret=0
    for co in combinations(basecom, min(k, len(basecom))):
        tmp = 0
        for c in co:
            tmp += bit[c]

        cnt=0
        for b in bits:
            if tmp & b == b:
                cnt+=1
        ret=max(ret, cnt)

    print(ret)


