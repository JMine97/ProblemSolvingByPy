"""
정확도 33.3
효율성 66.7


"""

def solution(gems):
    answer = []

    gems_set = set(gems)

    len_gems_set = len(gems_set)

    minimum = 1000000

    gems_dict = {}


    start = 0
    end = 0

    while end < len(gems):
        if gems[end] not in gems_dict:
            gems_dict[gems[end]] = 1
        else :
            gems_dict[gems[end]] += 1

        
        end += 1
        
        if len_gems_set == len(gems_dict):

            while start < end :
                if gems_dict[gems[start]] > 1 :
                    gems_dict[gems[start]] -= 1
                    
                    start += 1
                    
                elif minimum > end - start:
                    minimum = end - start
                    answer = [start+1, end]
                    
                    break
                
                else:
                    break
                

        
    
    return answer


print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA",
                "EMERALD", "SAPPHIRE", "DIA"]))
