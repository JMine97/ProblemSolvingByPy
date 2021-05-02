'''
조합 -> 각 개수 count  combinations(List, num)

Orders 의 크기: 2 <= len(Orders) <= 20
Course의 크기 : 1 <= len(Course) <= 10
** 둘 다 적은 양의 input이라 여유로워 보이지만, 여유롭지 않은 시간이 주어진 문제이다. 

Combination을 하면서 orders에 따른 숫자만큼 새로운 list를 생성해내기 때문에 그 길이는 Factorial 단위로 커지므로 2^n의 좋지 않은 시간복잡도를 가지므로 적은 양의 input이지만 list로 풀게 되면 1초를 벗어나 시간초과가 남.

Combination의 연산횟수 : n! / r!(n-r)!

Big-O : O(len(course) * (len(orders) * 최대 combination연산회수))
        = O(20*10*20C10+a) # 20C10은 대략 18.5만회
'''

from itertools import combinations

def solution(orders, course): 
    answer = []
    for num in course:
        d = {} # 개수를 사용할 수 있는 방법 중 dict을 사용(Counter는 라이브러리 제한 가능성, 그리고 중복 된 최다수 다루기 까다로움.)
        li = []
        for order in orders:
            li.extend(list(combinations(sorted(order), num)))
        
        for t in li: # combination을 한 것을 다 담은 길이 
            t = ''.join(t)
            if t in d:
                d[t] += 1
            else:
                d[t] = 1
        

        for k, v in d.items():
            if max(d.values()) > 1 and max(d.values()) == v:
                answer.append(k)
                
    answer.sort()
    return answer
