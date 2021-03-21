import re

n = int(input())
p = re.compile('(100+1+|01)+')

for i in range(n):
  checklist = str(input())
  
  if p.fullmatch(checklist):
    print('YES')
  else:
    print('NO')
