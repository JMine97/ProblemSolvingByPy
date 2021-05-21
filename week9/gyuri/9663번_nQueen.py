# n-queen
# *****  PyPy3으로      *****
'''
퀸은 상하좌우 대각선 방향으로 이동 가능
Backtracking 알고리즘
> ‘유망한 노드들만 검사하고, 유먕하지 않다면 부모 노드로 돌아가 탐색을 계속한다'

0.)퀀이 올 수 있는 모든 경우의 수를 두고, 그 중에서 답을 찾는 방법
N = 4 가정,
각 퀸은 한 열의 하나씩만 올 수 있기 때문에
점검해야 할 모든 경우의 수는 4 * 4 * 4 * 4 = 256가지 입니다.-> 탐색할 필요가 없는 경우까지 탐색하여 비효율적

1.) 백트래킹
dfs,bfs 으로 특정 노드에서 유망성을 점검하고,
유망하지 않다면 그 노드의 부모로 돌아가서 다음 노드에 대한 검색을 계속하게 되는 절차입니다.

유망성 검사 규칙을 정해야한다.
- 같은 열에 있으면 안된다.
- 같은 '/'대각선에 있으면 안된다.
- 같은 '\'대각선에 있으면 안된다.
'''
import sys
input = sys.stdin.readline

n = int(input())

def dfs(row):
    global count
    if row == n:
        count += 1   # 백트래킹을 통해서 마지막까지 도달했기 때문에 count += 1
        return
    for col in range(n):
        queen[row] = col    # 행에 모든 경우의 수를 넣는다. (row, col) 위치에 퀸을 놓으면
        for i in range(row):    # 대각선과 열에 퀸이 있는 확인
            if queen[i] == queen[row] or abs(queen[i]-queen[row]) == row - i:
                break
        else:
            # `else :` 는 break 를 만나지 않고 무사히 `for i in range (row)`을 통과하면 실행된다.
            # 즉 퀸이 현재 위치에 있어도 된다는 의미로 검사를 진행한다.
            dfs(row + 1)

queen = [0] * n
count = 0
dfs(0)
print(count)

# 복잡도 : ???
