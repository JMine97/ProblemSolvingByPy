# 문자열 처리를 regex를 이용해서 함. 

import sys

s = str(input())
check = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f',':']
for ch in s:
    if ch not in check:
        sys.exit(0)


ans = []
s = s.split(":")

if s.count("") >= 2:
    while s.count("") > 1:
        s.remove("")
for i in range(len(s)):
    if s[i] == '':
        while len(s) < 8:
            s.insert(i, '0000')
            


for sp in s:
    if len(sp) == 4:
        ans.append(sp)
        continue
    else: 
        while len(sp) < 4:
            sp = '0' + sp
        ans.append(sp)


print(":".join(ans))
