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
    
    reverseFlag = True 
    for c in comm:
        if c == 'R':
            if reverseFlag == False:
                reverseFlag = True
            else: 
                reverseFlag = False
        elif c == 'D':
            if reverseFlag and q:
                q.popleft()
            elif reverseFlag == 0 and q:
                q.pop()
            else:
                print("error")
                break
    
    
    answer = list(q)
    if reverseFlag == False:
        answer = answer[::-1]
        
    answer = str(answer)
    answer = answer.replace(" ", "")
    print(answer)
