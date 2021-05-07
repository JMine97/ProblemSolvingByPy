'''
1. 전치행렬 만들기 list(map(list, zip(*relation)))
2. append는 ()안 요소 전체를 추가 하지만
   extned는 ()안 요소 하나하나를 접근해 배열에 추가
3. set()으로 만들 값은 변형 불가능한 값이어야 하기 때문에 원소들을 tuple로 변형시킨다
4. 최소성 만족을 위해 set(j).issubset(i)
   ex) j=[1,2,2] i=[1,2,3] 일 때도 = (하위집합 j에 중복되는 원소가 있을 때도) 
       상위집합의 부분집합으로 인정하기 위해 set(j)를 붙여주는 걸로 추정
'''

from itertools import combinations
def solution(relation):
    relation = list(map(list, zip(*relation))) #전치행렬
    r = len(relation)
    c = len(relation[0])
    answer = []
    can = []
    for i in range(1, r + 1):
        #append() 전체 append
        #extend() iterable 요소 각각 접근해서 추가
        can.extend(combinations(range(r), i))
    #can
    #[(0,), (1,), (2,), (3,), (0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3), (0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3), (0, 1, 2, 3)]

    # 유일성
    key = []
    for i in can:
        tmp = []
        for j in i:
            tmp.append(relation[j])

        # set의 원소는 변형이 불가능한 값이어야한다
        # 때문에 set으로 변형할 안의 원소들이 튜플이어야함
        can_key = list(map(tuple, zip(*tmp)))
        if len(set(can_key)) == c:
            key.append(i)
    key.sort(key=lambda x: len(x))
    #key
    #[(0,), (0, 1), (0, 2), (0, 3), (1, 2), (0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3), (0, 1, 2, 3)]

    # 최소성
    for i in key:
        flag = True
        for j in answer:
            if set(j).issubset(i):
                flag = False
                break
        if flag:
            answer.append(i)
    
    return len(answer)
