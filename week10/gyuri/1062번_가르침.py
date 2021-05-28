# 1062번_가르침.py
'''
K개의 글자 저장 가능
읽을 수 있는 단어 개수의 최댓값
모든 단어는 anta 로 시작하며 tica로 끝남

[풀이] 
set()을 통해서 단어에 배운 알파벳이 포함되는 지 확인하는 백트래킹. 
'''
import sys
input = sys.stdin.readline
answer = 0
n, k = map(int, input().split())
if k < 5 or k == 26:
    answer = 0 if k < 5 else n
    print(answer)
    exit(0)
words = []
for _ in range(n):
    temp = input()
    words.append(temp[4:len(temp)-5]) # 앞 뒤에 반복되는 부분은 자르고 list에 넣는다.

learn = set('antic')

def dfs(idx, cnt):
    global answer
    # 배울 수 있는 알파벳의 개수 도달. 단어를 읽을 수 있는 지 check
    if cnt == k - 5:
        check = 0
        for word in words:
            for a in word:
                if set(a) - learn:
                    break
            else:
                check += 1
        answer = max(answer, check)
        return
    # 백트래킹을 통해서 모든 경우의 수를 확인 
    for i in range(idx, 26):
        alpha = chr(97 + i)
        if set(alpha) - learn:
            learn.add(alpha) # set의 add(), remove() 모두 O(1)
            dfs(i, cnt + 1)
            learn.remove(alpha)


dfs(0, 0)
print(answer)

# -----------틀린 풀이!!--------------
'''
각 단어별로 알아야하는 알파벳을 구한다.
알파벳의 갯수를 dict에 넣는다.
최대값 k개를 선택한다.
근데 이럴 경우에 단어를 읽을 수 있다고 보장할 수가 없다...흠
'''
import sys
input = sys.stdin.readline
answer = 0
word = []
n, k = map(int, input().split())
for _ in range(n):
    temp = input()
    word.append(temp[4:len(temp)-5])

word_set = set('antic')
alpha_dict = {}
for w in word:
    temp = set(w) - word_set
    for i in list(temp):
        if i in alpha_dict.keys():
            alpha_dict[i] += 1
        else :
            alpha_dict[i] = 1
alpha_dict = sorted(alpha_dict.items(), key=(lambda x : x[1]), reverse=True)
k = k - 5
if k <= 0:
    print(answer)
    sys.exit()
i = 0

while k > 0 and i < len(alpha_dict):
    word_set.add(alpha_dict[i][0])
    i += 1
    k -= 1

for w in word:
    if list(set(w)-word_set):
        continue
    answer += 1
print(answer)
