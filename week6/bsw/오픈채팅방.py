# O(record)

def solution(record):
    answer = []
    
    info = {}
    state = []
    for re in record:
        input_line = re.split()
        # 0: 상태 // 1: ID // 2: NickName
        if input_line[0] == 'Enter':
            info[input_line[1]] = input_line[2]
            state.append((input_line[1], 'in'))
            
        elif input_line[0] == 'Leave':
            state.append((input_line[1], 'out'))
            
        elif input_line[0] == 'Change':
            info[input_line[1]] = input_line[2]
            
    for s in state:
        ID, move = s
        if move == 'in':
            answer.append("%s님이 들어왔습니다."%(info[ID]))
        elif move == 'out':
            answer.append("%s님이 나갔습니다."%(info[ID]))
        
    return answer