from collections import defaultdict
from itertools import combinations

def solution(orders, course):
    answer=[]
    
    for c in course:
        dic=defaultdict(int)
        for o in orders:
            for com in list(combinations(sorted(o), c)):
                dic[com]+=1

        if dic:
            m=max(dic.values())
            for k, v in dic.items():
                if v==m and v>=2:
                    answer.append(''.join(k))

    return sorted(answer)
