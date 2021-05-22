# 1759번_암호만들기.py
'''
1. L개의 알파벳 소문자들로 구성
2. 최소 한 개의 모음(a, e, i, o, u) and 최소 두 개의 자음으로 구성
3. 정렬된 문자열
복잡도: O(n^2)
'''
import sys
from itertools import combinations
input = sys.stdin.readline

l, c = map(int, input().split())
pw = list(map(str, input().split()))
pw.sort()
vowel = ['a', 'e', 'i', 'o', 'u']
# 모음이 몇개 있는지 골라내기
answer = list(combinations(pw, l))
check = set()
for a in answer:
    count_v = 0
    for i in a:
        if i in vowel:
            count_v += 1
    if count_v < 1 or len(a) - count_v < 2:
        continue
    check.add(a)
check = list(check)
check.sort()
for i in check:
    print(''.join(i))
