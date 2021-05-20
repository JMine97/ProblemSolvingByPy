import sys
input=sys.stdin.readline

'''
그냥 combination 라이브러리로 풀어도 됩니다

알파벳이 증가하는 중
최소 한 개의 모음과 최소 두 개의 자음
암호 전체길이 l
'''

l, c = map(int, input().split())
cand=list(input().split())
cand.sort()

def password(word, cur):
    if len(word)==l:
        vowel='aeiou'
        cnt_vowel=0
        for w in word:
            if w in vowel:
                cnt_vowel+=1
        cnt_not_vowel=l-cnt_vowel

        if cnt_vowel>=1 and cnt_not_vowel>=2:
            print(word)
        return

    for i in range(cur+1, c):
        password(word+cand[i], i)

password('', -1)


