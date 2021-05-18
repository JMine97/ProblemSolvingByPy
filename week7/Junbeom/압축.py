def solution(msg):
    answer = []
    dic = {}
    for i in range(26):
        dic[chr(65+i)] = i+1 # 1번 조건
    
    left, right = 0, len(msg)

    while True:
        m = msg[left:right]
        if m in dic.keys():
            answer.append(dic[m])
        
            if right >= len(msg):
                return answer
        
            dic[m+msg[right]] = len(dic)+1
            left += len(m)
            right = len(msg)
        else:
            right -= 1
