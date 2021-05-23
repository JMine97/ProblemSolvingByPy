import sys
from itertools import combinations
input = sys.stdin.readline

l, c = map(int, input().split())
li = list(input().rstrip().split())
li.sort() # 빠른 조회를 위해 
vowel = ['a', 'e', 'i', 'o', 'u']

p  = combinations(li, l)

def isPromising(line): # sorting이 된 것인지, 그리고 자음이 2개 이상 모음이 1개 이상인지 조회 
    
    if list(line) != sorted(line):  # tuple을 sorted하면 list가 됨. 
        return False # sorting이 안되어있으면 false 리턴
    vo, con = 0, 0 # 모음, 자음 
    for l in line:
        if l in vowel:
            vo += 1
        else: con += 1
    if vo >= 1 and con >= 2: 
        return True # Promising 

for line in p:
    if isPromising(line):
        print(''.join(line))


