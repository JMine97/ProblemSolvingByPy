from collections import deque
def solution(cacheSize, cities):
    answer = 0

    if cacheSize == 0:
        return len(cities) * 5
    
    deq = deque()
    cities = deque(cities)
    
    while cities:
        c = cities.popleft().lower()
        if c in deq:
            answer += 1
            deq.remove(c)
            deq.append(c)
        else:
            answer += 5
            deq.append(c)
        if len(deq) > cacheSize:
            deq.popleft()
            
    return answer

'''
도시이름 검색 -> 맛집 게시물
DB 캐시를 적용할 때 캐시 크기에 따른 실행시간 측정 
cacheSize: 캐시 크기
cities: 도시 이름 배열
배열을 순서대로 처리할 때 총 실행시간 
deque를 통해서 캐시를 큐를 통해서 처리하자
from collections import deque
deque의 크기를 제한 
복잡도 : O(N)
'''

