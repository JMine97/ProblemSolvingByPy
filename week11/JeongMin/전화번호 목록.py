import sys
input=sys.stdin.readline

for _ in range(int(input())):
    arr=[]
    for _ in range(int(input())):
        arr.append(input().strip())
    arr.sort() #요소마다 숫자가 작은 순서로, 길이가 짧은 순서로 정렬된다

    flag=True
    for i in range(len(arr)-1):
        if arr[i]==arr[i+1][:len(arr[i])]:
            print('NO')
            flag=False
            break
    if flag:
        print('YES')