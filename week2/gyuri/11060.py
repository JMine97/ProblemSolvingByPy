import sys

input = sys.stdin.readline
n = int(input())
maze = list(map(int, input().split()))
memory = [9999] * n
memory[0] = 0

for i in range(n):
    step = maze[i]
    for j in range(1, step + 1):
        if i+j >=n:
            memory[n - 1] = min(memory[n-1], memory[i]+1)
        else:
            memory[i + j]=min(memory[i+j], memory[i]+1)

if memory[-1] == 9999:
    print('-1')
else:
    print(memory[-1])

