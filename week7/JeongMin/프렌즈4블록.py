'''
O(n^2)
1. 전치행렬을 만들어주기 위해 list(map(list, zip(*board)))
1-1. zip()은 tuple을 반환하는데 tuple은 값 변경이 안 되니 list로 바꿔줌
1-2. map()은 주소값을 반환하기 때문에 list()로 묶어줌
2. 중복되는 원소를 넣지 않기 위해 set() / set.add()
'''

import copy

def solution(m, n, board):
    answer = 0
    board = list(map(list, zip(*board))) #*는 리스트를 unpacking 한다
    
    while True:
        remove=set()
        for i in range(len(board)-1):
            for j in range(len(board[i])-1):
                if board[i][j]!='_' and board[i][j]==board[i+1][j]==board[i][j+1]==board[i+1][j+1]:
                    remove.add((i, j))
                    remove.add((i+1, j))
                    remove.add((i, j+1))
                    remove.add((i+1, j+1))
                    
        if not remove:
            break

        answer+=len(remove)

        for k in remove:
            i, j=k
            board[i][j]='_'

        for i in range(len(board)):
            front, back=[],[]
            for j in range(len(board[i])):
                if board[i][j]=='_':
                    front.append('_')
                else:
                    back.append(board[i][j])
            board[i]=front+back
    
    
    return answer
