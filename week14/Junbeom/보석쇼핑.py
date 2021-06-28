def solution(gems): # 가장 짧은 거리 
    l = len(set(gems)) # 보석의 개수
    
    left, right = 0, 0 # 투포인터 
    dic = {}
    dic[gems[0]] = 1 # dic 초기화 
    result = [0, len(gems)-1] # 제일 긴 범위를 잡아놓음. 
    
    
    while left < len(gems) and right < len(gems): # 두 개의 포인터가 진열대의 범위를 벗어나지 않는 선에서 
        if len(dic) == l: # 딕셔너리에 담긴 값이 보석의 개수와 같다면, left를 이동시켜서 더 짧은 길이를 찾아야 함. 
            if right-left < result[1]-result[0]: # 중복이 존재할 수 있는 수. 
                result = [left, right] # result 변경
            
            if dic[gems[left]] == 1: 
                del dic[gems[left]]
            else:
                dic[gems[left]] -= 1
            left += 1
            
        else: # 딕셔너리에 담긴 값이 보석의 개수가 같지 않으면 right를 이동시켜서 범위를 늘림. 
            right += 1
            if right == len(gems):
                break
            if gems[right] in dic.keys():
                dic[gems[right]] += 1
            else:
                dic[gems[right]] = 1
            
    return [result[0]+1, result[1]+1]
