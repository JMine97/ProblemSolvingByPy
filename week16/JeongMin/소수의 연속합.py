def prime_list(n):
    li = [True] * (n+1)

    for i in range(2, int(n ** 0.5) + 1):
        if li[i] == True:  # i가 소수인 경우
            for j in range(i*2, n+1, i):  # i이후 i의 배수들을 False
                li[j] = False

    return [i for i in range(2, n+1) if li[i] == True]

n = int(input())
prime_number = prime_list(n)

m=len(prime_number)
end=0
cnt=0
sumv=0
#투 포인터
for start in range(m):
    while end<m and sumv<n:
        sumv+=prime_number[end]
        end+=1

    if sumv==n:
        cnt+=1

    sumv-=prime_number[start]

print(cnt)



