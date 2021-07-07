import sys
input=sys.stdin.readline

tree=[i//2 for i in range(2013+1)]

t=int(input())

for _ in range(t):
    a, b = map(int, input().split())
    while a!=b:
        if a>b:
            a//=2
        else:
            b//=2

    print(a*10)