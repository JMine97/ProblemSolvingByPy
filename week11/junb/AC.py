from collections import deque
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    comm = str(list(input().rstrip()))
    n = int(input().rstrip())
    li = list(input().rstrip())
    if comm.count("D") > n: # 만약 길이보다 더 많은 양을 delete하면
        print("error") # error 리턴
        continue    
    q = deque()
    for l in li:
        if l not in ["[", "]", ","]:
            q.append(int(l))
    
    for c in comm: # 명령이 차례대로 들어올 떄, 
        if c == 'R': # Reverse 명령어가 들어오면 뒤집기. 
            if q: # 안에 값이 있으면, 
                q = deque(list(q)[::-1]) # 뒤집고 다시 queue로 만들어주기 
            else: 
                print("error")
                continue
        elif c == 'D': # Delete 명령어가 들어오면 맨 앞 pop. 
            if q:
                q.popleft() 
            else: 
                print("error")
                continue

    answer = str(list(q))
    answer = answer.replace(" ", "")
    print(answer)
