# 시간초과
# 왜?

string = input()
bomb = input()

answer = ''

for i in range(len(string)):
    answer+=string[i]
    if string[i] == bomb[-1]:
        if answer[-len(bomb):] == bomb:
            answer = answer[:-len(bomb)]

if answer == '':
    print('FRULA')
else : print(answer)

