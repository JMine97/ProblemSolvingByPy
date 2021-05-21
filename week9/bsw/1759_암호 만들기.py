'''
알파벳 L개
모음최소 1개 자음최소 2개
오름차순
중복없음


모든 경우의 수 에서 모음1개미만, 자음 2개미만의 경우를 제외
'''

L, C = map(int, input().split())
arr = list(input().split())
from itertools import combinations

comb_arr = list(combinations(sorted(arr), L))

mo = set(['a', 'e', 'i', 'o', 'u'])
for comb in comb_arr:
    c = set(comb)
    if not mo&c or len(comb)-len(mo&c)<2:
        continue

    print(''.join(comb))
