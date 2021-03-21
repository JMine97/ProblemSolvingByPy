n,m = map(int,input().split())
lst = []

for _ in range(n):
    lst.append(input())

k = int(input())

max_count = 0

for row in range(n): # 각 행에 대해서

    #그 행의 0의 개수를 셈
    zero_count = 0
    for i in lst[row]:
        if(i == '0'): 
            zero_count += 1
            
    #킬 수 있는 행의 개수 찾기
    if k >= zero_count and zero_count%2 == k%2: # 행의 0 개수가 홀수 일 때 k도 홀수 0 개수가 짝수 일 때 k도 짝수이면 그 행을 켜진 상태로 만들수 있음

        #이 행과 똑같은 구조를 가진 행을 모두 찾음
        row_count = 0
        for sub_row in range(n):
            if lst[sub_row] == lst[row]:
                row_count += 1

        # 그 중 최댓값을  찾음
        if row_count >= max_count:
            max_count = row_count
            
print(max_count)
        
