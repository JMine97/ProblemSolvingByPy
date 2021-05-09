def solution(relation):
    answer = []
    row = len(relation)
    col = len(relation[0]) # 4 (1 << 4 -> 10000)
    for i in range(1, 1<<col): #모든 조합에 대한 검사
        
        isMinimal = True # 최소성을 판단하는 것임. -> '학번' 이라는 것이 이미 담겨있으면, '학번,이름'은 안됨.
        for num in answer:
            if num & i == num: # AND 연산자로 확인. 겹치는 것이 있으면 num을 반환. 
                isMinimal = False
                break
        
        if isMinimal: # 최소성을 만족했으면 유일성을 확인하는 작업. 
            s = set()
            for j in range(row): #모든 사람을 돌면서
                cand = "" # 후보키가 될 수 있는 키.
                for k in range(col): #모든 key에 대해 탐색. 0, 1, 2, 3
                    if i & (1<<k):
                        cand += str(relation[j][k])
                s.add(cand)
                print(s)
                if len(s) == row:
                    answer.append(i)
    print(answer)
    return len(answer)
