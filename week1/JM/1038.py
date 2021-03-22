import sys
input=sys.stdin.readline

n=int(input())
arr=[i for i in range(10)]

i=1
while True:
    if i>1022:
        break
    back=arr[i]%10
    for j in range(back):
        arr.append(arr[i]*10+j)

    i+=1


arr.sort()
print(arr)
if n>len(arr)-1:
    print(-1)
else:
    print(arr[n])

    
