def solution(info, query):
    #info : 지원자 정보
    #query : 조건
    # [조건]을 만족하는 사람 중 코딩테스트 점수를 X점 이상 받은 사람은 모두 몇 명인가?
    
    answer = []
    

    #쿼리 개수 만큼 반복
    for i in range(len(query)):
        count = 0

        # java and backend and junior and pizza 100 = > ['java', 'backend', 'junior', 'pizza', '100']
        q = query[i].split(" and ")
        last = q[-1].split(" ")
        q.pop()
        q = q + last


        # 각 유저에 대해서
        for data in info:
            for j in range(len(q)):
                #이 쿼리의 모든 조건을 만족하면 count를 늘림
                if j == 4:
                    if int(q[j]) <= int(data.split()[-1]):
                        count += 1
                    
                if q[j] == "-":
                    continue

                # 하나라도 조건에 안맞는 유저면 버림
                elif j != 4 and data.find(q[j]) == -1:
                    break

                        
        answer.append(count)
        
    
    return answer


print(solution(["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150",
          "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"],
         ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200",
          "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100",
          "- and - and - and - 150"]))


"""
1. 주어진 info에 대해 '-'를 포함한 모든 만족하는 쿼리의 종류를 만든다.

java backend junior pizza 150

 -   backend junior pizza 150
java     -   junior pizza  150

2. 딕셔너리 구성

3. 주어진 query에 대해 딕셔너리를 확인하고,값이 있을 경우 lower bound를 통해 쿼리보다 점수가 같거나 높은 갯수 찾기



"""
