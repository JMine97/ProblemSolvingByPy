import copy
def solution(m, n, board):
    board = list(map(list, zip(*board)))
    
    def game(b):
        score = 0
        # 복사
        tempB = copy.deepcopy(b)
        
        for i in range(1,n):
            for j in range(1,m):
                if b[i][j] == -1: continue
                if b[i][j] == b[i-1][j] == b[i-1][j-1] == b[i][j-1]:
                    tempB[i][j], tempB[i-1][j], tempB[i-1][j-1], tempB[i][j-1] = 0,0,0,0
        
        for i,v in enumerate(tempB):
            # 점수 
            cnt = v.count(0)
            score += cnt
            # 사라지는 블록만큼 왼쪽을 '-1'으로 채운다.
            tempB[i] = [-1]*cnt + [a for a in v if a!=0]
        return tempB, score
    
    answer = 0
    while True:
        board, score = game(board)
        if score == 0:  return answer
        answer += score
        
'''
블록 2*2 -> 사라짐 + 점수 획득
복잡도 : O(n^3) 
'''
