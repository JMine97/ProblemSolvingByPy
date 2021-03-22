n = int(input())

li = list(range(0, 10))
count = -1

while li:
  count += 1
  num = li.pop(0)
  
  if count == n:
    break

  for i in range(10):
    if i < num%10:
      temp = num*10 + i
      li.append(temp)
    else:
      break

if n>=1023:
  print(-1)
else:
  print(num)

