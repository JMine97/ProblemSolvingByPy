import sys
from itertools import combinations

N, K = map(int, input().split())
words = [set(input()) - {'a', 'n', 't', 'i', 'c'} for _ in range(N)]  
#print(words)
if K < 5:
    print(0)
    sys.exit()

alphabet = set("abcdefghijklmnopqrstuvwxyz")

# 필수알파벳
must_alphabets = {'a', 'n', 't', 'i', 'c'}

alpha_set = alphabet - must_alphabets

alpha_combs = combinations(alpha_set, K-5)

answer = 0
for comb in alpha_combs:
    comb = set(comb)
    cnt = 0
    for word in words:
        if word.issubset(comb): # word <= comb
            cnt += 1
    
    #최대값 갱신
    if cnt > answer:
        answer = cnt

print(answer)