def solution(cacheSize, cities):
    
    from collections import deque
    # 조건이 여러개 주어졌을 때 마지막 조건도 else대신 elif로 작성하자
    # 오류가 생길경우 찾기 힘들다
    #
    # O(len(cities))
    # 
    # 도시명 소문자로 통일
    #   if 캐시 메모리에 빈공간이 있을 때
    #       if 캐시메모리에 city가 이미 있는 경우
    #           해당 인덱스 삭제        
    #           append(city)
    #           실행시간 +1
    #       elif 없는 경우
    #           append
    #           실행시간 +5
    #   elif 캐시 메모리가 가득 찼을 때
    #       if 캐시메모리에 city가 이미 있는 경우
    #           해당 인덱스 삭제        
    #           append(city)
    #           실행시간 +1
    #       elif 없는 경우
    #           popleft
    #           append
    #           실행시간 +5
    
    
    if cacheSize == 0:
        return 5*len(cities)
        
    cache = deque()
    time = 0
    for city in cities:
        city = city.lower()
        if len(cache) < cacheSize:
            if city in cache:
                cache.remove(city)
                cache.append(city)
                time +=1
            elif city not in cache:
                cache.append(city)
                time +=5
        elif len(cache) == cacheSize:
            if city in cache:
                cache.remove(city)
                cache.append(city)
                time +=1
            elif city not in cache:
                cache.popleft()
                cache.append(city)
                time+=5
    
    return time