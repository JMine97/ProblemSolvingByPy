'''
운영체제 페이지 테이블 관련 지식이 필요했던 문제. 
- 검색이 가능했던 테스트였기 때문에 잘 알려진 LRU 알고리즘을 사용함. 
- cacheSize 가 0인 문제점을 해소하고 대소구분 조건만 조절하면 금방 풀 수 있음.

input 사이즈를 보면, cacheSize 가 30이내, 도시의 수가 100000개가 주어졌다. 

for문이 한번만 돌 게 되는 풀이이므로, 도시의 수가 N 이라 할 때 해당 문제의 시간복잡도는 O(N).

'''

def solution(cacheSize, cities): # 10만개. LRU, 대소구분 없이 -> lower()
    cache = []
    t = 0
    if cacheSize == 0:
        return 5*len(cities)
    for city in cities:
        city = city.lower()
        # Miss
        if not city in cache:
            t += 5
            if len(cache) < cacheSize:
                cache.append(city)
            else:
                if cache:
                    cache.pop(0)
                cache.append(city)
        # Hit
        else:
            t += 1
            cache.pop(cache.index(city))
            cache.append(city)
        # print(cache)
    return t
