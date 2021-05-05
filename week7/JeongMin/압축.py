'''
O(n)
'''
def solution(msg):
    answer = []
    dict={}
    for i in range(0, 26):
        dict[chr(ord('A')+i)]=i+1
    
    i, num=0, 27
    w=''
    while i<len(msg):
        w+=msg[i]
        if w not in dict:
            answer.append(dict[w[:-1]])
            dict[w]=num
            num+=1
            w=''
            continue
        if i==len(msg)-1:
            answer.append(dict[w])
            
        i+=1
    return answer
