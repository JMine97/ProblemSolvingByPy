from itertools import combinations
def solution(relation):
    relation = list(map(list, zip(*relation)))
    r = len(relation)
    c = len(relation[0])
    answer = set()
    can = []
    for i in range(1, r + 1):
        can.extend(combinations(range(r), i))

    # 유일성
    key = []
    for i in can:
        tmp = []
        for j in i:
            tmp.append(relation[j])
        can_key = tuple(map(tuple, zip(*tmp)))
        if len(set(can_key)) == c:
            key.append(i)
    key.sort(key=lambda x:len(x))

    # 최소성
    for i in key:
        flag = True
        for j in answer:
            if set(j).issubset(i):
                flag = False
                break
        if flag:
            answer.add(i)
    
    return len(answer)
