'''
시간복잡도 O(n)
record의 최대 길이 10^5
'''

def solution(record):
    answer = []
    dict={}
    
    for r in record:
        rr = r.split()
        if rr[0] in ['Enter','Change']:
            dict[rr[1]]=rr[2]
    
    for r in record:
        rr = r.split()
        if rr[0]=="Enter":
            answer.append(dict[rr[1]]+"님이 들어왔습니다.")
        elif rr[0]=="Leave":
            answer.append(dict[rr[1]]+"님이 나갔습니다.")
            
    return answer
