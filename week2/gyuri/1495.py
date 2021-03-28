n, s, m = map(int, input().split())
v = list(map(int, input().split()))

# dp 를 위한 list 변수 초기화
dp1 = [0 for i in range(m + 1)] # 초기화는 0으로, 이전 볼륨이면 1
dp2 = [0 for i in range(m + 1)] # temp 변수로 사용할 예정

# 시작 볼륨, s 를 표시
dp1[s] = 1
for i in v:
    for j in range(m + 1):
        # 이전 볼륨이라면 비교 
        if dp1[j]:
            if j + i <= m:
                dp2[j + i] = 1
            if i - i >= 0:
                dp2[j - i] = 1
    dp1 = dp2
    dp2 = [0] * (m + 1)

answer = -1
# 마지막 n번째 곡에 대한 볼륨이 저장되어 있는 dp1, 역순으로 for문을 돌려 가장 큰 볼륨을 출력. 없을 경우 -1 출력

for i in range(m, -1, -1):
    if dp1[i]:
        answer = i
        break
print(answer)

