import sys
input = sys.stdin.readline
n, k = map(int, input().split())
'''
k개를 넘지 않는 비어있지 않은 물병
초기 상태 1리터씩

## 2 ** (bin(n)[::-1].index('1'))
'''

ret=0
while bin(n).count('1')>k:
    a = 2 ** (bin(n)[::-1].index('1'))
    ret += a
    n += a
print(ret)
