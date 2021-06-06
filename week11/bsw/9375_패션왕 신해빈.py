
t = int(input())

for _ in range(t):

    n = int(input())
    clothes = {}
    for _ in range(n):
        cloth, kind = input().split()

        if kind not in clothes.keys():
            clothes[kind] = []
        
        clothes[kind].append(cloth)

    ans = 1
    for key in clothes.keys():
        ans*=len(clothes[key])+1
    
    print(ans-1)