import sys
input=sys.stdin.readline
'''
??? 직전과 직후 상태를 안다면 사다리를 만들 수 있다

-는 가로막대가 있는 경우, *은 가로막대가 없는경우
'''

k=int(input())
n=int(input())
end=list(input().strip())
front=[chr(ord('A')+i) for i in range(k)]

ladder=[]
for _ in range(n):
    ladder.append(input().strip())

### ? 앞 부분
for l in range(len(ladder)):
    if ladder[l][0] == '?':
        break
    for kk in range(k-1):
        if ladder[l][kk]=='-':
            front[kk], front[kk+1] = front[kk+1], front[kk]


### ? 뒷 부분
for l in range(len(ladder)-1, -1, -1):
    if ladder[l][0] == '?':
        break
    for kk in range(k-1):
        if ladder[l][kk]=='-':
            end[kk], end[kk+1] = end[kk+1], end[kk]


ret=[]
for i in range(k-1):
    if front[i]!=end[i]:
        ret.append('-')
        front[i], front[i+1] = front[i+1], front[i]
    else:
        ret.append('*')

if front==end:
    print(''.join(ret))
else:
    print('x'*(k-1))