
N, M = map(int, input().split())

train = list([0]*20 for _ in range(N))
print(train)
for _ in range(M):
    line = list(map(int,input().split()))

    if line[0] == 1:
        i, x = line[1], line[2]
        train[i-1][x-1] = 1

    elif line[0] == 2:
        i, x = line[1], line[2]
        train[i-1][x-1] = 0

    elif line[0] == 3:
        i = line[1]
        tmp=[0]
        tmp.extend(train[i-1][:-1])
        train[i-1] = tmp

    elif line[0] == 4:
        i = line[1]
        tmp=[]
        tmp.extend(train[i-1][1:])
        train[i-1] = tmp
        train[i-1].append(0)

train_str = set()

for t in train:
    train_str.add(''.join(str(t)))
print(train_str)
