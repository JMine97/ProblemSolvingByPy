'''
input의 길이는 1000 이하 
시간복잡도 : O(N^2)
'''

def solution(s):
    answer = len(s)
    if len(s) < 2: 
      return len(s)
    for word in range(1, len(s)//2+1):
      res = ''
      count = 1
      temp = s[:word]

      for i in range(word, len(s)+word, word):
        if temp == s[i:i+word]:
          count += 1
        else:
          if count == 1:
            res += temp
          else:
            res = res + str(count) + temp
          temp = s[i:i+word]
          count = 1
      answer = min(answer, len(res))
    return answer 
