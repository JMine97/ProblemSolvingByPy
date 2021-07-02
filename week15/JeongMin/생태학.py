'''
import sys 안 쓰면 오류 나는 것으로 보임
'''
from collections import defaultdict
import sys
input=sys.stdin.readline

dic=defaultdict(int)
total=0
while True:
    tree=input().rstrip()
    if not tree:
        break
    dic[tree]+=1
    total+=1

dic=sorted(dic.items())
for k, v in dic:
    print(k, '%.4f' %round((v/total)*100, 4))