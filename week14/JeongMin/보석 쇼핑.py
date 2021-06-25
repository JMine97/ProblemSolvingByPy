'''
투 포인터 알고리즘
'''

from collections import defaultdict
def solution(gems):
    gems_len=len(set(gems))
    dic=defaultdict(int)
    dic[gems[0]]=1

    answer=[]
    start=0; end=0

    while start<len(gems) and end<len(gems):
        if len(dic)==gems_len: #길이저장
            answer.append([start, end])
            dic[gems[start]]-=1
            if dic[gems[start]]==0 : del dic[gems[start]]
            start+=1
        else:
            end += 1
            if end==len(gems) : break
            dic[gems[end]]+=1

    answer.sort(key=lambda x:((x[1]-x[0]), x[0]))
    return [answer[0][0]+1, answer[0][1]+1]