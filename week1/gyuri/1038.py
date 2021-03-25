import sys
N = int(input())
count = -1

def solution(digit, sub):
    global count
    if len(sub)-1 == digit:
        count += 1
        if count == N:
            answer = int(sub)
            print(answer)
            sys.exit()
        return
    else:
        for i in range(int(sub[-1])):
            if digit - len(sub) <= i:
                # 남은 자리수는 i 보다 작아야 감소하는 숫자를 계속 만들 수 있다.
                solution(digit, sub+str(i))

for i in range(0,10):
    for j in range(0,10):
        solution(i,str(j))
print('-1')

