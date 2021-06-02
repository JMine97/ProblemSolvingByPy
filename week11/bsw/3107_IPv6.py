string = input()

arr = string.split(':')

answer = []

# 생략된 0 을 붙이는 작업
for a in arr:
    str_len = len(a)
    if str_len < 4:
        a = '0'*(4-str_len) + a
    answer.append(a)

print(answer)
# 생략된 그룹을 추가
len_ans = len(answer)

if len_ans < 8:
    for _ in range(8-len_ans):
        answer.insert(answer.index('0000'), '0000')

#'::' 이 문자열 맨 앞이나 맨 뒤에 오는경우
# ex)0000:0001:0002:0003:0004:0005:0006:0007 => ::1:2:3:4:5:6:7
if len_ans > 8:
    for _ in range(len_ans-8):
        answer.remove('0000')

print(':'.join(answer))

