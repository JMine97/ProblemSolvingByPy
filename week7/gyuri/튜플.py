import re
from collections import Counter

def solution(s):
    answer = []
    s = Counter(re.findall('\d+', s))
    # print(s) 
    # Counter({'2': 4, '1': 3, '3': 2, '4': 1})
    for k, v in sorted(s.items(), key=lambda x: x[1], reverse=True):
        answer.append(int(k))
    return answer
