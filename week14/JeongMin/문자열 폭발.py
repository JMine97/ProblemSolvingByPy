'''
1차 시도 : re.sub 연산은 문자열을 당겨옴 (시간초과)
2차 시도 : stack (맞음)
'''
st=input()
bomb=input()
stack=[]

for s in st:
    stack.append(s)
    if s==bomb[-1] and ''.join(stack[-len(bomb):])==bomb:
            del stack[-len(bomb):]


if len(stack)==0:
    print("FRULA")
else:
    print(''.join(stack))
