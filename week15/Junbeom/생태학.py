import sys # 없으면 EOFError 발생. 
input= sys.stdin.readline

dic = {}
count = 0 

while True:
    s = input().rstrip()
    if not s:
        break
    count += 1 # count 가 더해지는 위치 조심할 것. 탈출 명령 밑에 있을 것. 
    if s in dic:
        dic[s] += 1
    else:
        dic[s] = 1

d = sorted(dic.items())

for k, v in d:
    value = round((v/count)*100, 4)
    print(k, '%.4f' %value)

