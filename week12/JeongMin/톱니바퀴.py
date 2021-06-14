'''
입력 12시방향부터 시계방향 순으로
N극 0 S극 1
시계방향 1, 반시계방향 -1

맞닿은 톱니바퀴 극이 다르면 반대방향 회전
'''

'''
split() 사용시 통으로 하나의 문자로 인식됨

반례)
11001110
10000101
01111110
01101111
4
2 -1
2 -1
2 1
2 1
정답 10
'''

wheel = []

for _ in range(4):
    wheel.append(list(map(int, input())))

# 회전
for _ in range(int(input())):
    num, dir = map(int, input().split())
    num -= 1
    pre_front = wheel[num][-2]
    pre_end = wheel[num][2]

    if dir == 1:
        wheel[num] = [wheel[num][7]] + wheel[num][0:7]
    else:
        wheel[num] = wheel[num][1:] + [wheel[num][0]]

    k = -2
    pre_d = dir
    # 앞으로
    for i in range(num - 1, -1, -1):
        if pre_front != wheel[i][k*-1]:
            pre_front = wheel[i][k]
            if pre_d == 1:  # 반대로 회전
                wheel[i] = wheel[i][1:] + [wheel[i][0]]
            else:
                wheel[i] = [wheel[i][7]] + wheel[i][0:7]
            pre_d *= -1
        else:
            break

    k = 2
    pre_d = dir
    # 뒤로
    for i in range(num + 1, 4):
        if pre_end != wheel[i][k*-1]:
            pre_end = wheel[i][k]
            if pre_d == 1:  # 반대로 회전
                wheel[i] = wheel[i][1:] + [wheel[i][0]]
            else:
                wheel[i] = [wheel[i][7]] + wheel[i][0:7]
            pre_d *= -1
        else:
            break

score = 0
for i in range(4):
    if wheel[i][0] == 1:
        score += 2 ** i
print(score)
