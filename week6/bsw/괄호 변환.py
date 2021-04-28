# 솔직히 재귀문제 시간복잡도 재는법을 잘 모르겠습니다
# 아마 p*log(p)가 아닐까요...?

def check_valance(p):
    left = 0
    right = 0
    for i in range(len(p)):
        if p[i] == '(':
            left +=1
        elif p[i] == ')':
            right +=1
        if left == right:
            return True
    return False
        
    
def check_correct(p):
    flag=0
    for i in range(len(p)):
        if p[i] == '(':
            flag +=1
        elif p[i] == ')':
            flag -=1
        if flag < 0:
            return False
    return True


def change_distance(p):
    a = ''
    # 해당 인덱스에 해당하는 문자열을 직접 변경할 수 없다
    # 빈 문자열에 추가하거나 슬라이싱 하는 방식을 사용해야함
    for i in range(len(p)):
        if p[i] == '(':
            a += ')'
        elif p[i] == ')':
            a += '('
    return a
        
    
def seperate_str(p):
    if len(p) == 0:
        return ''
    
    left = 0
    right = 0
    for i in range(len(p)):
        if p[i] == '(':
            left +=1
        elif p[i] == ')':
            right +=1
        if left == right:
            u = p[:i+1]
            v = p[i+1:]

            if check_correct(u):
                return u + seperate_str(v)
            elif not check_correct(u):
                string = '(' + seperate_str(v) + ')'
                u = u[1:-1]
                string += change_distance(u)
                return string
                
    
def solution(p):
    return seperate_str(p)
    
