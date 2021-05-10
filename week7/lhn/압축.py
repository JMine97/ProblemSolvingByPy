"""
o(n)
"""

def solution(msg):
    dic = dict()
    lst = []

    #초기화
    [lst.append(chr(i)) for i in range(ord('A'), ord('Z')+1)]

    
    for idx, char in enumerate(lst):
        dic[char] = idx+1
    idx = 0
    maxIdx = 26
    length = 0
    answer = []

    while True:
        length += 1
        
        #딕셔너리에 현재 문자열이 없을 때
        if not msg[idx:idx+length] in dic:
            #추가
            answer.append(dic[msg[idx:idx+length-1]])

            #딕셔너리 마지막 위치에 새로운 문자열 추가
            maxIdx += 1
            dic[msg[idx:idx+length]] = maxIdx
            #시작 위치 변경
            idx += length-1
            
            length = 0

        #있을 때
        else:
            # 마지막 값 추가
            if idx+length-1 == len(msg):
                answer.append(dic[msg[idx:idx+length-1]])
                break

    return answer

