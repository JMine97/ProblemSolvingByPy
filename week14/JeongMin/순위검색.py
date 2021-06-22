'''
###defaultdict 사용
##장 : 딕셔너리에 키 값이 없어도 바로 사용 가능하다

from collections import defaultdict

#int defaultdict를 만들 때
int_dict=defaultdict(int)
int_dict['key1']
int_dict['key2']=1
>>defaultdict(<class 'int'>, {'key1':0, 'key2':1})

#list difaultdict를 만들 때
list_dict=defaultdict(list)
list_dict['key1']
list_dict['key2']='test'
list_dict >> defaultdict(<class 'list'>, {'key1':[], 'key2':'test'})
'''

#내가 들어갈 수 있는 부분을 모두 수집한 후
#key_value : 포함되는 학생의 점수
#거기서 명 수 구함

from collections import defaultdict
from itertools import combinations

def solution(info, query):
    dict = defaultdict(list)
    for i in info:
        i = i.split()
        dict_key = i[:-1]
        dict_val = int(i[-1])
        for size in range(0, 5):
            for c in combinations(dict_key, size):
                tmp_key = ''.join(c)
                dict[tmp_key].append(dict_val)

    for key in dict.keys():
        dict[key].sort()

    answer = []
    for q in query:
        q = q.replace('and ', '').replace('- ', '').split()
        st = ''.join(q[:-1])
        score = int(q[-1])

        if st not in dict:
            answer.append(0)
            continue

        scores = dict[st]
        left = 0
        right = len(scores)
        while left < right:  # 이상이므로
            mid = (left + right) // 2
            if scores[mid] >= score:
                right = mid
            else:
                left = mid + 1
        answer.append(len(scores) - left)
    return answer


