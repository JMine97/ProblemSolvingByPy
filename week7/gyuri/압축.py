def solution(msg):
    answer = []
    dic = {}
    
    # 26개의 문자 입력
    for i in range(1,27):
        dic[chr(64+i)] = i

    i, count = 0, 0
    while True:
        count += 1
        if count == len(msg):
            answer.append(dic[msg[i:]])
            return answer
        # dic에 없으면 추가하고 append하고 
        if msg[i:count+1] not in dic:
            dic[msg[i:count+1]] = len(dic) + 1
            answer.append(dic[msg[i:count]])
            i = count
        # dic에 있으면 i 를 유지해서 더 킨 문자도 압축 가능한 지 check

    return answer
'''
복잡도 : O(n)
'''
