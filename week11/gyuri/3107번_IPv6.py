# 3107번_IPv6.py
'''
IPv6의 길이 : 128비트, 32자리, 16진수, 4자리, 클론(:)으로 구분
1. 0으로 시작하면 0 생략, 전체가 0이면 0으로 축약
2, 0으로만 이루어져 있는 그룹이 한개이상 연속이면 ::으로 바꿀 수 있다. 이 규칙은 한번만 사용가능
-> 축약을 복원하라
'''
# 3107번_IPv6.py
'''
IPv6의 길이 : 128비트, 32자리, 16진수, 4자리, 클론(:)으로 구분
1. 0으로 시작하면 0 생략, 전체가 0이면 0으로 축약
2, 0으로만 이루어져 있는 그룹이 한개이상 연속이면 ::으로 바꿀 수 있다. 이규칙은 한번만 사용가능
-> 축약을 복원하라
'''
import sys
input = sys.stdin.readline
answer = ''
hex = input().rstrip('\n').split(':')
hex_len = len([v for v in hex if v])

# 규칙 2
if hex_len != 8:
    for i in range(len(hex)):
        if hex[i] == '':
            hex = hex[:i] + ['0000'] * (8 - hex_len) + hex[i:]
            break

hex = ' '.join(hex).split()

for i in range(len(hex)):
    if len(hex[i]) == 4:
        continue
    hex[i] = "0" * (4 - len(hex[i])) + hex[i]

answer = ':'.join(hex)
print(answer)

# -----------------------------------------------
S = input().split(":")
for i in range(len(S)):
    if S[i] == ' ':
        S[i] = "0000"
    if len(S[i]) < 4:
        S[i] = "0"*(4-len(S[i]))+S[i]
if len(S) < 8:
    for i in range(8-len(S)):
        S.insert(S.index("0000"), "0000")
if len(S) > 8:
    del S[S.index("0000")]
print(":".join(S))
