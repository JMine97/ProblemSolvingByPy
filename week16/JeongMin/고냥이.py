from collections import defaultdict
n=int(input()) #인식할 수 있는 최대 알파벳의 종류
st=input()
dic=defaultdict(int)

ret=0
end=0
for start in range(len(st)):
    while end<len(st) and len(dic)<=n:
        if len(dic)==n and st[end] not in dic:
            break
        dic[st[end]]+=1
        end+=1

    if len(dic)<=n:
        ret=max(ret, end-start)

    dic[st[start]]-=1
    if dic[st[start]]==0:
        del dic[st[start]]

print(ret)
