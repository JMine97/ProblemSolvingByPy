s='cdcd'

from collections import deque

stack=deque()

for ss in s:
    stack.append(ss)

    if len(stack)>=2 and stack[-1]==stack[-2]:
        stack.pop()
        stack.pop()


if not stack:
    print(1)
else:
    print(0)