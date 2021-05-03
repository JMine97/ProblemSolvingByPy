#문제에서 하라는 대로 하면됨
# 시간복잡도는 O(N)
record = list(input().replace("[","").replace("]","").split(","))

def solution(record):
    answer = []
    temp = []
    temp2 = []
    user = dict()
    
    for i in range(len(record)):
        keyword = record[i].replace('"',"").split()

        if keyword[0] == "Leave":
            temp2.append("님이 나갔습니다.")
            temp.append(keyword[1])
            
        elif keyword[0] == "Enter":
            user[keyword[1]] = keyword[2]
            temp.append(keyword[1])
            temp2.append("님이 들어왔습니다.")
   
        else :
            user[keyword[1]] = keyword[2]

    for i in range(len(temp)):
        answer.append(user[temp[i]]+temp2[i])
        
            
    return answer 

