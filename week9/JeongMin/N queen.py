'''
반드시 n개의 퀸을 체스판 위에 놓아야 합니다.
그렇지 않으면 카운트 하지 않습니다.

퀸을 기준으로 위/아래/대각선 방향에는 놓으면 안 됨
행번호 차이 = 열번호 차이면 같은 대각선상
n개의 퀸, n*n 크기 체스판
'''
n=int(input())

def check(i): #위/아래/대각선 방향에 퀸이 있는지 확인 #있으면 true 리턴
    for j in range(i):
        if row[j] == row[i] or abs(row[j]-row[i]) == (i-j):
            return True
    return False

def queen(i):
    if i==n:
        global result
        result+=1
        return

    for j in range(n): #row 배열의 인덱스 : row / row 배열의 값 : col
        row[i]=j
        if not check(i):
            queen(i+1)

result=0
row = [0]*15
queen(0)
print(result)
