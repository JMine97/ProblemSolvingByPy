string = input()
bomb = input()

answer = ''

string = 's'*500000 + '4'*500000
bomb = 'ssssssssssssssssss444444444444444444'
for i in range(len(string)):
    answer+=string[i]
    if string[i] == bomb[-1]:
        if answer[-len(bomb):] == bomb:
            answer = answer[:-len(bomb)]

if answer == '':
    print('FRULA')
else : print(answer)

