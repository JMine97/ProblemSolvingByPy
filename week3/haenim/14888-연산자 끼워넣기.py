n = int(input())
nums = list(map(int, input().split()))
add, sub, mul, div = map(int , input().split())

min_, max_ = 1e9, -1e9

def dfs(i, res, add, sub, mul, div):
    global max_, min_
    if i == n:
        max_ = max(res, max_)
        min_ = min(res, min_)
        return

    else :
        #+연산자가 남아있으면 더하고 add 수 줄이고
        if add:
            dfs(i+1, res+nums[i], add-1, sub, mul, div)
            
        if sub:
            dfs(i+1, res-nums[i], add, sub-1, mul, div)
            
        if mul:
            dfs(i+1, res*nums[i], add, sub, mul-1, div)
            
        if div:
            dfs(i+1, int(res/nums[i]), add, sub, mul, div-1)

dfs(1, nums[0], add, sub, mul, div)
print(max_)
print(min_)
            
    
