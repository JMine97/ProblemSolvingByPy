import sys
sys.setrecursionlimit(10**9)
input=sys.stdin.readline

n=int(input())
a=list(map(int, input().split()))
calc=list(map(int, input().split())) #덧뺄곱나
max_v=-1e9
min_v=1e9

def bt(ret, cnt):
    if cnt==n:
        global max_v, min_v
        max_v=max(max_v, ret)
        min_v=min(min_v, ret)
        # print(ret)
        return

    if calc[0]>0:
        calc[0]-=1
        bt(ret+a[cnt],cnt+1)
        calc[0]+=1

    if calc[1]>0:
        calc[1]-=1
        bt(ret-a[cnt],cnt+1)
        calc[1]+=1

    if calc[2]>0:
        calc[2]-=1
        bt(ret*a[cnt],cnt+1)
        calc[2]+=1

    if calc[3]>0:
        calc[3]-=1
        if ret<0:
            tmp=-ret//a[cnt]
            tmp=-tmp
        else:
            tmp=ret//a[cnt]
        bt(tmp,cnt+1)
        calc[3]+=1


bt(a[0], 1)
print(max_v); print(min_v)