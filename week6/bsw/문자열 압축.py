# O(length^2)

def solution(s):
    
    length = len(s)
    
    # j가 탐색을 마칠경우 종료
    answer = [length]
    for i in range(1, length//2 +1):
        comp = s[:i]
        cnt =1
        string = ''
        for j in range(i, length+1, i): #
            
            cur = s[j : j+i]

            if comp == cur:
                cnt +=1
            else:
                if cnt == 1:
                    cnt = ''
                string += str(cnt) + comp
                comp = cur
                cnt = 1
            
            #why?????????????????????????????????????????????
            if comp and len(comp)<i:
                string+=comp
            
        answer.append(len(string))
    return min(answer)