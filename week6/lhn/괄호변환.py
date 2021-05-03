#문제에서 하라는 대로 하면 됨
#시간복잡도는 O(n)

#u,v로 나누기
def divide(p):
    u = ""
    v = ""
    left = right = 0
    
    for i in range(len(p)):
        if p[i] == "(":
            left += 1

        else :
            right += 1

        if left == right:
            u=p[:i+1]
            v = p[i+1:]
            return u,v
        
#u가 올바른 괄호인지 판단
def isCorrect(u):
    count = 0
    for i in u:
        if i == "(":
            count += 1
        else:
            count -= 1
            if count < 0:
                return False
    return True

def solution(p):
    a = ''

    #1번 과정
    if p == "":
        return ""

    #2번과정
    u,v = divide(p)

    #3번과정
    if isCorrect(u):
        return u + solution(v)

    # 4번 과정
    else :
        a = "("
        a += solution(v)
        a += ")"
        u = u[1:-1]

        for i in range(len(u)):
            if u[i] == "(":
                a += ")"
            else :
                a+= "("

        return a
            
        
    return a

print(solution("()))((()"))
