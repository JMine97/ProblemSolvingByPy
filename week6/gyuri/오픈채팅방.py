def solution(record):
    answer = []
    d = {}
    for r in record:
        word = list(map(str, r.split()))
        if word[0][0] == 'E' or word[0][0] == 'C':
            # uid가 존재 check -> 아이디 업데이트
            d[word[1]] = word[2]    
    for r in record :
        word = list(map(str, r.split()))
        if word[0][0] == 'E':
            nick = d[word[1]] + '님이 들어왔습니다.'
            answer.append(nick)
        elif word[0][0] == 'L':
            nick = d[word[1]] + '님이 나갔습니다.'
            answer.append(nick)

    return answer
'''
오픈채팅방 
관리자창
[닉네임]님이 들어왔습니다. 
[닉네임]님이 나갔습니다. 
## 닉네임 변경
# 채팅방을 나간 후, 새로운 닉네임으로 다시 들어간다.
# 채팅방에서 닉네임을 변경한다. 

닉네임을 변경하면 기존에 출력도 전부 변경

Enter, Leave, Change
'''
