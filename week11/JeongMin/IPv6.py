import sys
input=sys.stdin.readline

ip=input().strip().split(':')
n=len(ip)

for i in range(len(ip)):
    if len(ip[i])==0:
        ip[i]='0000'
    elif len(ip[i])!=0:
        ip[i]='0'*(4-len(ip[i]))+ip[i]

if len(ip)<8:
    [ip.insert(ip.index('0000'), '0000') for _ in range(8-len(ip))]
if len(ip)>8:
    ip.remove('0000')
print(':'.join(ip))