def solution(s):
    answer = len(s)
    length = len(s)//2+1
    print(answer)
    for step in range(1, length):
        com = ""
        count = 1
        prev = s[0:step]
        for j in range(step,len(s), step):
            if prev == s[j:j+step]:
                count+=1
            else :
                # 현재까지의 압축을 저장, count == 1이면 숫자없이 저장 
                com+= str(count)+prev if count >=2 else prev
                # 다시 상태 초기화
                count = 1
                prev = s[j:j + step]
        com+= str(count)+prev if count >=2 else prev
        answer = min(answer, len(com))
            
    return answer
