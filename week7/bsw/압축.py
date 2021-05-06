# O(len(msg))

def solution(msg):
    answer = []
    dic = {}
    
    for i in range(1, 27):
        dic[chr(i+64)] = i
    #print(dic)
    tmp = ''
    for m in msg:
        tmp += m # A
        #print(tmp)
        if tmp not in dic:
            dic[tmp] = len(dic)+1
            answer.append(dic[tmp[:-1]])
            tmp = tmp[-1]
            
    answer.append(dic[tmp]) 
    
    return answer