#14888 연산자 끼워넣기


N = int(input())
lst = list(map(int, input().split()))

# + - * //
sym = list(map(int, input().split()))

MAX = -999999999
MIN = 999999999

def dfs(num, depth):
    if depth == N:
        global MAX
        global MIN
        MAX = max(num, MAX)
        MIN = min(num, MIN)
    
    for i in range(4):
        if sym[i] > 0:
            sym[i]-=1
            if i == 0:
                dfs(num + lst[depth], depth+1)
                
            if i == 1:
                dfs(num - lst[depth], depth+1)
                
            if i == 2:
                dfs(num * lst[depth], depth+1)
                
            if i == 3:
                # 문제에서 요구하는 음수 계산법과 파이썬 내장 계산법이 다르다
                if num < 0:
                    dfs(-(abs(num) // lst[depth]), depth+1)
                else:
                    dfs(num // lst[depth], depth+1)
            sym[i]+=1
    
dfs(lst[0], 1)

print(MAX)
print(MIN)    



