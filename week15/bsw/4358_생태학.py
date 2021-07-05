import sys
input = sys.stdin.readline

d= {}
total=0
while 1:
    tree=input().strip('\n')
    if not tree:
        break
    
    if tree not in d:
        d[tree] = 0
    d[tree] += 1
    total += 1
    
# print(total)

# 이거왜안됨????????
# 반례 : 50.00
# 쓰레기 같은 문제
# for key in sorted(d):
#     print(key, round((d[key]*100)/total, 4))

dic=sorted(d.items())
for k, v in dic:
    print(k, '%.4f' %round((v/total)*100, 4))
