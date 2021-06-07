# 참가자 k
k = int(input())

# 가로줄 n
n = int(input())

# 원하는 결과
result = input()

# 사다리 모양
ladders = [input() for _ in range(n)]

'''
0 1 2 3 4 5 6 7 8 9
A B C D E F G H I J
   -
 0 1 2 3 4 5 6 7 8

1. 출발점에서 내려가면서 사다리를 탐색
2. 각 사다리에서 '-'와 만났을 경우 문자열 배열의 해당 idx 와 idx+1 을 swap
3. ? 라인을 만나는 순간 break
4. 도착점에서 올라가면서 사다리를 탐색
5. 2~4번 반복
6. ? 라인의 직전 직후 문자열 상태를 비교하여 중간의 사다리를 유추가능

O(n*k)
'''

start = [ord('A')+i for i in range(k)]
end = [ord(rst) for rst in result]
# print(start)
# print(end)

# 위에서 출발
for ladder in ladders:
    if '?' in ladder:
        break
    for i in range(len(ladder)):
        if ladder[i] == '-':
            start[i], start[i+1] = start[i+1], start[i]

# 아래서 출발
for ladder in ladders[::-1]:
    if '?' in ladder:
        break
    for i in range(len(ladder)):
        if ladder[i] == '-':
            end[i], end[i+1] = end[i+1], end[i]

# print('------')
# print(start)
# print(end)


# ? 라인의 직전 직후 문자열을 비교
# 인덱스 i-1과 i에 해당하는 부분이 교차하여 같으면 '-'
# 그렇지 않으면 '*'
ans = []
for i in range(1, k):
    if start[i-1] == end[i] and end[i-1] == start[i]:
        ans.append('-')
    else:
        ans.append('*')

# 알아낸 ? 라인을 start에 적용하여 end와 비교
for i in range(len(ans)):
    if ans[i] == '-':
        start[i], start[i+1] = start[i+1], start[i]


if start == end:
    print(''.join(ans))
else:
    print('x'*(k-1))
