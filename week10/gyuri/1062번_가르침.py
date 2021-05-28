# 1062번_가르침.py
'''
K개의 글자 저장 가능
읽을 수 있는 단어 개수의 최댓값
모든 단어는 anta 로 시작하며 tica로 끝남

해결
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
