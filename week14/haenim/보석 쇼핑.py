"""
정확도 33.3
효율성 13.3

"""

def solution(gems):
    answer = []

    gems_set = set(gems)

    len_gems_set = len(gems_set)

    minimum = 1000000

    value = [0]*len_gems_set
    gems_dict = dict(zip(gems_set,value))

    print(gems_dict)

    start = 0
    end = 0

    while end < len(gems):
        temp = gems[start:end+1]
        gems_dict[gems[end]] += 1

        
        end += 1
        
        if len_gems_set == len(set(temp)):

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
