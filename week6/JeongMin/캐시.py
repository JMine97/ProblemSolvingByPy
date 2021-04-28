'''
cities의 최대 크기는 10^5, 최대 cachesize는 30 이므로
10^6*3의 시간복잡도를 갖는 알고리즘이 완성된다
'''

from collections import deque

def solution(cacheSize, cities):
    answer = 0
    cache_hit, cache_miss=1, 5
    q=deque()
    
    for c in cities:
        s=c.lower()
        if s in q:
            answer+=cache_hit
            q.remove(s) #q에서 값 s 제거
            q.append(s)
        else:
            answer+=cache_miss
            q.append(s)
        
        if len(q)>cacheSize:
            q.popleft()
        
    return answer
