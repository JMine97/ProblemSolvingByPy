n,m = map(int, input().split())
s = []
check = []
count = 0

for i in range(n):
    s.append(input())

for i in range(m):
    check = input()
    if check in s:
        count += 1
    

print(count)
