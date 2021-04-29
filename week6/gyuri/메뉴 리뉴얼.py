from itertools import combinations
def solution(orders, course):
    answer = []

    for i in course:
        d = {}
        for j in orders:
            com = list(combinations(sorted(list(j)),i))
            for c in com :
                c = ''.join(c)
                if c in d:
                    d[c] += 1
                else :
                    d[c] = 1
        # 만들수 있는 조합 중 max 
        if d:
            m = max(d.values())
            if m < 2:
                continue
            for k,v in d.items():
                if m==v:
                    answer.append(k)
    return sorted(answer)

'''
단품 -> 코스요리, 순서 상관없으니깐 조합 combinations
두번 이상 세트로 주문되어야 메뉴 후보에 포함
코스요리를 구성하는 단품의 갯수가 담긴 배열
'''

'''
d = {}
for i in course:
    for j in orders:
        com = ''.join(sorted(combinations(list(j),i)))
        if com in d:
            d[com] += 1
        else :
            d[com] 만들기

'''
