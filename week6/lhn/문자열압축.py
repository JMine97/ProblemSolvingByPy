"""
문자열 압축

abcabcdede

a b c a b c d e d e => 10

ab ca bc de de
=> ab ca bc 2de => 9

abc abc ded e
=> 2abc ded e => 8

몇개 단위로 잘라야 가장 작은 문자열이 나올까
그 때의 문자열 길이를 구해라

=> 모두 다 계산해봐야 최솟값을 구할 수 있다



1. 자르는 단위를 늘려가면서 문자열을 자른다

2. 잘라진 문자열에서 겹치는 부분을 처리해서 문자열 길이를 구한다

3. 이전의 문자열 길이와 현재 문자열 길이를 비교해 최솟값을 찾는다


for문이 2개 쓰였기 때문에 시간 복잡도는 O(n^2)

"""

def solution(s):
    answer = 100000
    
    for i in range(1,len(s)+1): #자르는 단위를 늘려가면서 계속 반복
        new_answer = 0 
        split = []

        # 1. 그 길이 만큼 문자열을 잘라서 리스트에 저장
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

print(solution("aabbbc"))
