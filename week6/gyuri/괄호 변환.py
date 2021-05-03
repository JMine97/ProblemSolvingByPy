'''
문제 : 괄호의 개수는 맞지만 짝이 맞지 않는다 -> 모든 괄호를 뽑아서 올바른 순서대로 배치된 괄호 문자열 return
함수 (w)
0. if w 빈 문자열 
    return 빈 문자열
w = u + v
//w ->  균형 잡힌 u , v로 분리 // 이때 u는 더이상 분리될 수 없는 균형잡힌 괄호 
if u is 균형 and 올바른 :
    return u + 함수(v)
else // u가 !올바른:
    #새로운 문자열 만들기
    new + (
    함수(v) -> 그러면 올바른 v가 돌아온다.
    ')를 붙임
    # ( + 올바른 v + )
    u의 첫번째와 마지막 문자를 제거하고, 
    나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙임????
    return 뉴 문자열
'''
from collections import deque
def solution(p):
    answer = ''
    # a[::-1] 를 원하는게 아니라 '(' -> ')', ')'->'(' 로바꾸라는 의미  
    def reverse(strings):
        r = {"(":")", ")": "("}
        rev= ''
        for s in strings:
            rev += r[s]
        return rev
    
    def func(w):
        func_answer =''
        if w == '':
            return ''
        left,right, i = 0,0,0
        # 균형으로 자르자 
        while True:
            if w[i] == '(':
                left += 1
            else :
                right +=1 
            if left == right :
                break
            i+=1   

        # u 가 올바른지 -> stack? append, pop 
        u = deque(w[0:i+1])
        s = deque()
        flag = 1
        while u:
            q = u.popleft()
            if q == '(':
                s.append(q)
            else:
                if not s:
                    flag = 0
                    break
                else:
                    s.pop()
        
        if flag and not s:
            func_answer += w[0:i+1]+func(w[i+1:])
            return func_answer
        else:
            # !올바른이면, stack 안에 있는 괄호들이 짝을 만나지 못해서 empty s 가 아니면
            func_answer += '(' + func(w[i+1:]) + ')'+ reverse(w[1:i])
            return func_answer
            
    answer = func(p)
    return answer
'''
시간복잡도 : O(N)
p는 '(' 와 ')' 로만 이루어진 문자열이며 길이는 2 이상 1,000 이하인 짝수
'''
