"""
암호는 최소 한개의 모음과 최소 두개의 자음으로 구성
알파벳이 암호에서 증가하는 순서로 배열(abc o bac x)

=> 전체 다 해보는데 조건에 맞지 않으면 빼면 됨

O(n)

"""



l, c = map(int, input().split())


alpha = list(map(str,input().split()))
alpha.sort()


def dfs(idx, lst):
    if idx == l: 
        vow = 0 # 모음 개수
        con = 0 # 자음 개수

        for i in range(l):
            if lst[i] in 'aeiou' : #모음이면 모음 증가
                vow += 1
                
            else : #자음이면 자음 증가
                con += 1

        if vow < 1 or con < 2 : # 조건 만족 못하면 버림
            return

        print("".join(lst))#조건 만족하면 출력
        
    else :
        for i in range(idx,c): 
            if lst and ord(lst[-1]) >= ord(alpha[i]) : #오름차순이 아니면 버림
                continue

            dfs(idx+1, lst + [alpha[i]] )
            
dfs(0,[])
