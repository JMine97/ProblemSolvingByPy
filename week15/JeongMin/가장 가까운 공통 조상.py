import sys
input=sys.stdin.readline

t=int(input())

for _ in range(t):
    n=int(input()) #노드 수
    tree =[0 for _ in range(n+1)]

    #b의 부모가 a
    for _ in range(n-1):
        a, b = map(int,  input().split())
        tree[b]=a

    a, b = map(int, input().split())
    a_parents, b_parents = [a], [b]

    while len(set(a_parents)&set(b_parents))==0:
        ta=tree[a]
        tb=tree[b]

        a_parents.append(ta)
        b_parents.append(tb)

        a=ta
        b=tb

    print(list(set(a_parents)&set(b_parents))[0])