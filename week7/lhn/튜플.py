"""

{{2}, {2, 1}, {2, 1, 3}, {2, 1, 3, 4}}
{{2, 1, 3, 4}, {2}, {2, 1, 3}, {2, 1}}
{{1, 2, 3}, {2, 1}, {1, 2, 4, 3}, {2}}

=> [2,1,3,4]

=> 가장 많이 나온 숫자 순으로 튜플을 구성하자


"""

def solution(s):
    answer = []

    # {{2}, {2, 1}, {2, 1, 3}, {2, 1, 3, 4}} -> [2,2,1,2,1,3,2,1,3,4]
    lst = s.replace("{","").replace("}","").split(",")

    # [2,2,1,2,1,3,2,1,3,4] -> 2,1,3,4
    set_ = set(lst)
    

    dic = dict()
    for item in set_: # set_의 각 원소에 대하여
        #dic["해당원소 개수"] = 해당원소
        #ex) [2,2,1,2,1,3,2,1,3,4] => {4:2, 3:1, 2:3, 1:4 }
        dic[lst.count(item)] = item

    #원소 개수 순으로 내림차순 정렬
    count = sorted(dic.items(), reverse=True)

    # 원소개수가 많은 순으로 원소를 정렬해서 리스트로 만듦
    for key,value in count:
        answer.append(int(value))
        
    
    return answer

solution("{{2},{2,1},{2,1,3},{2,1,3,4}}")
