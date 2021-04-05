import sys
input = sys.stdin.readline

def dfs(node):
    global res_idx
    global flag
    if not flag:
        return
    if res[res_idx] != node:
        flag = False
        return
    res_idx += 1
    for i in arr[node]:
        if chk[i] == 0:
            chk[i] = 1
            dfs(i)

n = int(input())
arr = [[] for _ in range(n+1)]
chk = [0] * (n+1)
order = [0] * (n+1)
for _ in range(n-1):
    a,b = map(int,input().split())
    arr[a].append(b)
    arr[b].append(a)
# print(arr)
res = [0] + list(map(int,input().split()))
res_idx = 1
flag = True
for i in range(1,n+1):
    order[res[i]] = i #res값 기준으로 우선순위 매김

for i in arr:
    i.sort(key=lambda x:order[x]) #우선순위 별로 트리 재정렬
# print(arr)
chk[1] = 1
dfs(1)
print(1 if flag else 0)
