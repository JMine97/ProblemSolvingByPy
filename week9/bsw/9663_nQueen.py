N = int(input())
cnt=0
board = [0 for _ in range(N)]

def isOkay(col):
    for i in range(col):
        if board[col] == board[i] or col - i == abs(board[col] - board[i]):
            return False
    return True

def dfs(col):
    global cnt
    if col == N:
        cnt+=1
        return

    for i in range(N):
        board[col] = i

        if isOkay(col):
            dfs(col+1)

dfs(0)
print(cnt)