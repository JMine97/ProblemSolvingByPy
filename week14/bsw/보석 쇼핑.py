# set 함수를 활용하려 했으나 시간복잡도가 O(N)인것을 고려해야 한다 -> 시간초과
# dict의 길이를 활용하는 문제
# dict를 활용하면 O(1)의 시간복잡도로 중복제거 기능을 활용 할 수 있음

def solution(gems):
    answer = []
    
    cnt_gems = len(set(gems))
    cur_gems={}
    l, r = 0, 0
    
    while l<len(gems) and r<len(gems):
        
        if gems[r] not in cur_gems:
            cur_gems[gems[r]] = 1            
        elif gems[r] in cur_gems:
            cur_gems[gems[r]] += 1
        
        r+=1
        
        #print(cur_gems)
        
        if len(cur_gems) == cnt_gems:
            
            while l<r and len(cur_gems) == cnt_gems:
                answer.append((l,r))    
                if gems[l] not in cur_gems:
                    break
                elif gems[l] in cur_gems:
                    cur_gems[gems[l]] -= 1
                
                if cur_gems[gems[l]] == 0:
                    del cur_gems[gems[l]]
                
                l+=1      
        
    answer.sort(key = lambda x : (x[1]-x[0], x[0]))
    return [answer[0][0]+1, answer[0][1]]