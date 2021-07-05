N = int(input())
string = input()

l , r=0, 0
len_s = len(string)
answer=0
cur = {}
while l<=r and r<len_s:
   
    # print(l,r)
    # print(cur)
    # abbcaccba
    # l  r
    if len(cur) == N:
        if string[r] in cur:
            cur[string[r]] += 1
            r+=1
        else:
            cur[string[l]] -= 1
            if cur[string[l]] == 0:
                del cur[string[l]]
            l+=1
    
    # elif len(cur) > N:
    #     cur[string[l]] -= 1
    #     if cur[string[l]] == 0:
    #         del cur[string[l]]
    #     l+=1
    elif len(cur) < N:
        if string[r] not in cur:
            cur[string[r]] = 0
        cur[string[r]] += 1
        r+=1
    '''
    
    b : 1
    c : 1
    
    '''
    # 현재 저장된 부분 문자열의 길이
    summ=0
    for val in cur.values():
        summ+=val    

    answer = max(answer, summ)
    if r == len_s:
        break

print(answer)