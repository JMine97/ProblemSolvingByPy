#이진 변환 횟수 #제거된 0의 개수
def solution(s):
    zero=0
    cnt=0

    while 1:
        if s=='1':
            break

        zero+=s.count('0')
        s=s.replace('0', "")
        s=bin(len(s))[2:]
        cnt+=1

    return [cnt, zero]