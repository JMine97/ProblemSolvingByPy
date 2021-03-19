import sys
input=sys.stdin.readline

n=int(input())
cnt=-1

i=0
k = 1
while True:
    if n >= 1023:  # 1022: 9876543210
        print(-1)  # N번째 감소하는 수 x
        break

    i_list=str(i)
    if len(i_list)-1>int(i_list[0]):
        i=(int(i_list[0])+1)*10**(len(i_list)-1)
        continue

    flag = 1
    if len(i_list) == 1:  # 길이가 1이면 무조건 감소하는 수
        pass
    else:
        next_i = 0
        for j in range(len(i_list) - 1):
            if i_list[j] <= i_list[j + 1]:
                flag = 0
                next_i = (int(i_list[0:j + 1]) + 1) * 10 ** len(i_list[j + 1:])
                break
    # print(flag, end=' ')
    if flag==1:
        cnt+=1
    else:
        i=next_i
        continue
    # print(cnt, i)
    if cnt==n:
        print(i)
        break
    i+=1
