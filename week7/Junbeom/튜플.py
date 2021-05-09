def solution(s):
    answer = []
    s = s.split("},")

    for i in range(len(s)):
      s[i]= s[i].replace("{","").replace("}","") 
      print(s[i])
    new_s = []  
    for i in s:
      new_s.append(i.split(","))
    
    new_s.sort(key=len)
    
    for num in new_s:
      for n in range(len(num)):
        if int(num[n]) not in answer:
          answer.append(int(num[n]))
      
    return answer
