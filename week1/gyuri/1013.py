# 해님님, 준범님 코드 참고해서 코드 
import re

n = int(input())
p = re.compile('(100+1+|01)+')
result = []
for i in range(n):
    case = str(input())
    if p.fullmatch(case):
        result.append('YES')
    else:
        result.append('NO')
for i in range(n):
    print(result[i])
