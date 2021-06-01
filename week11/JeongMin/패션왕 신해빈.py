import sys
input=sys.stdin.readline

for _ in range(int(input())):
    dict={}
    for _ in range(int(input())):
        a, b = input().split()
        if b in dict:
            dict[b].append(a)
        else:
            dict[b]=[a]

    ret=1
    for v in dict.values():
        ret*=(len(v)+1) #해당 카테고리 물품 안 입는 경우 포함

    print(ret-1)