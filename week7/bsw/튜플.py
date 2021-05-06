# set() = 집합
#         따라서 집합연산이 사용가능
# O(len(s))

def solution(s):
    answer = []
    
    tmp = s.split('},{')
    
    tmp[0] = tmp[0][2:]
    tmp[-1] = tmp[-1][:-2]
    
    tmp2 = []
    for t in tmp:
        tmp2.append(list(map(int, t.split(','))))
        
    tmp2.sort(key = lambda x : len(x))
    
    for t in tmp2:
        answer.extend(set(t) - set(answer))
    
    
    

    return answer