'''
u, v를 어떻게 나누는 지 이해하고 순차적인 조건을 차근차근 해소하면서 풀면 되는 문제. 

시간 복잡도는 O(N)
'''

def divide(p):
  l_count = r_count = 0
  
  for i in range(len(p)):
    if p[i] == '(': l_count += 1
    elif p[i] == ')': r_count += 1

    if l_count == r_count:
      break

  return p[:i+1], p[i+1:] # u, v    

def isRight(s):
  result = True
  count = 0
  for i in range(len(s)):
    if s[i] == '(':
      count += 1
    elif s[i] == ')':
      count -= 1
    if count < 0:
      result = False
      break 
  
  return result


def solution(p):
  answer = ''
  if len(p) == 0:
    return '' # 1번 조건 
  
  u, v = divide(p) # 2번 조건
  if isRight(u) == True: # 3번 조건
    answer = u + solution(v) # 3-1번 조건
    return answer

  else : # false
    answer = '(' # 4-1번 조건
    answer += solution(v) # 4-2번 조건
    answer += ')' # 4-3번 조건

    u = u[1:-1] # 4-4번 조건
    for i in range(len(u)): 
      if u[i] == '(': answer += ')'
      elif u[i] == ')': answer += '('
  
  return answer # 4-5번 조건
