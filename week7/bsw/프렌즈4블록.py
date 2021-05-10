def solution(m, n, board):
    answer = 0
    Flag = True
    
    #b = list(map(list,zip(*board)))
    
    lst = []
    for j in range(n):
        tmp = ''
        for i in range(m, 0, -1):
            tmp += board[i-1][j]
        lst.append(tmp)
    
    zero_loc = {1}
    while zero_loc:
        zero_loc.clear()
        
        for i in range(len(lst)):
            for j in range(len(lst[i])):
                if j+1 >= len(lst[i]) or i+1>=len(lst) or j+1>=len(lst[i+1]):
                    continue
                if lst[i][j] == lst[i][j+1] == lst[i+1][j] == lst[i+1][j+1]:
                    zero_loc.add((i  ,j))
                    zero_loc.add((i  ,j+1))
                    zero_loc.add((i+1,j))
                    zero_loc.add((i+1,j+1))
                
        for i in range(len(lst)):
            tmp = ''
            for j in range(len(lst[i])):
                if (i,j) in zero_loc:
                    answer +=1
                    continue
                tmp+=lst[i][j]
            lst[i] = tmp

    return answer


solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"])

