N, S = map(int, input().split())
lst = list(map(int,input().split()))

l, r = 0, 0

answers = []
sum_nums = 0
while l<=r and r<N:
    print(lst[l], lst[r], sum_nums)
    
    if sum_nums < S:
        sum_nums+=lst[r]
        r+=1

    elif sum_nums >= S:
        answers.append(r-l)
        sum_nums-=lst[l]
        l+=1


if not answers:
    print(0)
else: print(sorted(answers)[0])
    
