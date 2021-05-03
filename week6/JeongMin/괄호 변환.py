def balance(u):
    if u.count('(')==u.count(')'):
        return True
    return False

def correct(u):
    stack=[]
    for i in u:
        if i=='(':
            stack.append(i)
        else:
            if not stack:
                return False
            stack.pop()
    return True
    
def reverse(u):
    ret=''
    for uu in u:
        if uu=='(':
            ret+=')'
        else:
            ret+='('
    return ret

def solution(p):
    u, v='',''
    
    if correct(p):
        return p
    
    for i in range(2, len(p)+1, 2):
        if balance(p[:i]):
            u, v = p[:i],p[i:]
            break
    if correct(u):
        return u+solution(v)
    else:
        return '('+solution(v)+')'+reverse(u[1:-1])
