"""

1. 자르는 단위를 늘려가면서 문자열을 자른다

2. 잘라진 문자열에서 겹치는 부분을 처리해서 문자열 길이를 구한다
ex) aabb => 2a2b

3. 이전의 문자열 길이와 현재 문자열 길이를 비교해 최솟값을 찾는다

for문이 2개 쓰였기 때문에 시간 복잡도는 O(n^2)

"""

def solution(s):
    answer = 100000
    
    for i in range(1,len(s)+1): 
        new_answer = 0 
        split = []

        # 1. 문자열을 잘라서 리스트에 저장
        for j in range(0,len(s),i): 
            split.append(s[j:j+i]) 

        #겹치는 문자열 개수 저장할 변수
        count = 1

        # 2. i개 단위로 잘랐을 때 문자열 길이 계산
        for j in range(len(split)-1):

            #현재 문자열과 다음 문자열이 같으면 count를 하나 증가
            if split[j] == split[j+1]:
                count += 1

            # 다르면 현재 문자열을 답에 추가하고 count 초기화
            else:
                
                # 겹치는 문자가 있었으면 답에 추가
                if count != 1:
                    new_answer += len(str(count))
                
                # 현재 문자열 길이를 답에 추가 
                new_answer += len(str(split[j]))
                count = 1

        # 마지막 부분 결과도 포함
        new_answer +=  len(str(split[-1]))
        if count != 1:
            new_answer += len(str(count))

        # 3. 자르는 단위를 늘려가면서 최솟값 찾기
        answer = min(answer, new_answer)
    
    return answer

print(solution("abcabcabcabcdededededede"))
