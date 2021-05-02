'''
input의 길이가 100000으로 짧지 않기 때문에 n^2 이하로 풀어야 한다. 
dict를 사용하여 검색 연산을 줄여야 시간초과를 내지 않을 수 있다. 같은 아이디어로 list로 풀이하였지만 시간초과에 걸렸다. 연산속도에 있어서 타 언어에 비해 불리하기 때문에 dict를 사용할 수 있는 상황이면 가급적 사용하도록 하자. 

시간 복잡도는 O(N)
'''

def solution(record):
    answer = []
    rec = []
    dict = {} # UID - name
    for i in range(len(record)):
        rec.append(record[i].split(" "))
        if rec[i][0] == "Enter" or rec[i][0] == "Change":
            dict[rec[i][1]] = rec[i][2] # dict(uid) = name
    
    for i in range(len(record)):
        temp = record[i].split(" ")
        if temp[0] == "Enter":
            answer.append(dict[temp[1]] + "님이 들어왔습니다.")
        elif temp[0] == "Leave":
            answer.append(dict[temp[1]] + "님이 나갔습니다.")
        
            
    return answer
