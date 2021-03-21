n = int(input())

li = list(range(0, 10))
count = -1

while True:
  count += 1
  num = li.pop(0)
  if count == n:
    break

  for i in range(10):
    if i < num%10:
      last = num*10 + i
      print("i, last is " + str(i) + " " +str(last))
      li.append(last)
      print("this is ")
      print(li)
      print("num is " + str(num))
    else:
      break

if n>=1023:
  print(-1)
else:
  print(num)

