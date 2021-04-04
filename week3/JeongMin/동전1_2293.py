import sys
input=sys.stdin.readline

def solution():
    n ,k = map(int, input().split())
    coin=[]
    for _ in range(n):
        coin.append(int(input()))
    result=[0 for _ in range(k+1)]
    result[0]=1

    for c in coin:
        for i in range(c, len(result)):
            result[i]=result[i]+result[i-c]
    # print(result)
    print(result[-1])

solution()

''''''''''''''''
  0 1 2 3 4 5 6 7 8 9 10
1 1 1 1 1 1 1 1 1 1 1 1
2 1 1 2 2 3 3 4 4 5 5 6
5 1 1 2 2 3 4 5 6 7 8 10
'''''''''''''''''

'''''''''''''''''
1, 2원을 썼을 때 5를 만드는 경우의 수를 구하는 방법은
1원만 써서 5원을 만들었을 때의 경우의 수 + 1, 2원을  3원을 만드는 경우의 수의 합이다

 
풀긴 풀었는데 더 깊은 이해 필요
'''''''''''''''''
