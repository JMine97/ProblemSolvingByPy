# 못 풀어서 디른 분의 풀이 참고함. 
# 기본 아이디어 : 입력 문자열에 하나씩 값을 담아, 스택에 푸쉬함. 그 다음 현재 문자가 폭탄의 마지막 글자와 같은지, 그리고 길이가 같은지를 판단하고 pop함.(삭제)
import sys
input = sys.stdin.readline

s = input().rstrip()
bomb = input().rstrip()

last = bomb[-1]
stack = []
l = len(bomb)

for ch in s: 
    stack.append(ch)
    if ch == last and ''.join(stack[-l:]) == bomb:
        del stack[-l:]

answer = ''.join(stack)

if answer == '':
    print("FRULA")
else:
    print(answer)


