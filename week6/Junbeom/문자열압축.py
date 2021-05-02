'''
input의 길이는 1000 이하 
시간복잡도 : O(N^2)
'''

def solution(s):
    answer = 1000000
    if len(s)== 1: 
      return 1
    for slicing in range(1, len(s)//2+1):
      res = ''
      cnt = 1
      tmp = s[:slicing]

      for i in range(slicing, len(s)+slicing, slicing):
        if tmp == s[i:i+slicing]:
          cnt += 1
        else:
          if cnt == 1:
            res += tmp
          else:
            res = res + str(cnt) + tmp
          tmp = s[i:i+slicing]
          cnt = 1
      answer = min(answer, len(res))
    return answer
