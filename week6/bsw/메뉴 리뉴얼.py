# combination을 사용해야 하기 때문에 시간복잡도를 따로 구하지 않고 풀이했습니다
# 풀이 후 제가 계산한 시간복잡도는 O(course * 2^orders) 입니다
# 이때 각 배열의 최대 길이는 orders = 20, course = 10, orders의 element = 10 이므로
# 최대 연산횟수는 약 수천만 회 정도로 예상됩니다
# 구현한 알고리즘에 따라 +@ 가 있을 수 있지만 countable 한 범위 내라고 판단됩니다.

def solution(orders, course):
    answer = []
    from itertools import combinations
    
    # string을 list처럼 사용할 수 있다 
    # sorted() 사용 가능
    # join을 활용하여 iterable의 element를 문자열로 만들수 있다
    # append : iterable을 통째로 추가
    # extend : iterable의 element를 추출하여 추가
    # dictinary 사용 연습
    #
    #
    # 1. orders의 모든 원소의 조합을 리스트에 담아 갯수를 센다
    # 2. 최대 갯수를 가지는 order를 result에 담는다
    # 2-1. 최대가 1인 경우 continue
    # 2-2. 최대값을 가지는 order가 여러개일 경우 모두 담는다
    
    
    for c in course:
        order_comb = []
        cnt_order_comb = {}
        for order in orders:
            # orders의 원소를 정렬한 뒤 combination
            # combination을 만들 수 없는 경우, 빈 list를 추가한다
            order_comb.extend(list(combinations(sorted(order), c)))
        
        for comb in order_comb:
            if comb not in cnt_order_comb.keys():
                cnt_order_comb[comb] = order_comb.count(comb)
        
        # 빈 list도 추가되었으므로 해당 경우를 제외하고 실행
        if cnt_order_comb:
            # value의 최대값을 구하고
            # 해당 value를 가진 key를 모두 answer에 추가함
            # join을 활용하여 튜플 형태의 데이터를 문자열로 만들어준다.
            v = cnt_order_comb.values()
            for key, value in cnt_order_comb.items():
                # 최대 주문 횟수가 1인 경우
                if value == 1:
                    continue
                # value가 최대 주문 횟수인 경우
                if value == max(v):
                    answer.append(''.join(key))
        
        answer.sort()
        
    return answer
