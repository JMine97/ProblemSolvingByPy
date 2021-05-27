'''
set()으로 해도 시간 초과는 나지 않을듯
일단, 비트 마스킹으로 풀어봤다
'''
import sys
input = sys.stdin.readline
n, m = map(int, input().split())


# 1 i x : i번째 기차에 x번째 좌석에 사람을 태움. 이미 사람이 있다면 행동 x
# 2 i x : i번째 기차에 x번째 좌석에 사람 내림. 사람이 없다면 행동 x
# 3 i: i번째 기차에 있는 승객 한칸씩 뒤로, 20번째에 사람 있으면 하차 + [False]
# 4 i : i번째 기차에 앉아있는 승객 한칸씩 앞으로, 1번째에 사람 있으면 하차
train = [0]*n
for _ in range(m):
    a = list(map(int, input().split()))

    if a[0] == 1:
        i, x = a[1] - 1, a[2] - 1
        train[i]=train[i]|1<<x

    elif a[0] == 2:
        i, x = a[1] - 1, a[2] - 1
        train[i] = train[i] & ~(1 << x) #해당 위치만 0으로 만듦

    elif a[0] == 3:
        i = a[1] - 1
        train[i]=train[i]<<1
        train[i] = train[i] & ~(1 << 20)

    elif a[0] == 4:
        i = a[1] - 1
        train[i] = train[i] >> 1

print(len(set(train)))
