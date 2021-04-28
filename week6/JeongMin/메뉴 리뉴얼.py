'''
시간복잡도 계산 질문하기
'''

from itertools import combinations

def solution(orders, course):
    answer = []
    
    for c in course:
        dict={}
        for o in orders:
            combination=list(combinations(sorted(o), c))
            for cc in combination:
                if cc in dict:
                    dict[cc]+=1
                else:
                    dict[cc]=1
                    
        if dict:
            v=max(dict.values())
            for key in dict:
                if v==dict[key] and dict[key]>=2:
                    answer.append("".join(key))
            
    answer.sort()
    return answer
