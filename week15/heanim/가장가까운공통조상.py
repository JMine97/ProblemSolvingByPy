T = int(input());


for i in range(T):
    N = int(input())
    node_info = [0]*(N+1)

    for i in range(N-1):
        parent, child = map(int,input().split())
        # [0, 8, 10, 16, 8, 8, 4, 6, 0, 5, 4, 10, 16, 1, 1, 6, 10]
        # 1의 부모는 8, 2의 부모는 10 ...
        node_info[child] = parent 
   
    n1, n2 = map(int,input().split())
    n1_ancestors, n2_ancestors = [n1],[n2]
    

    # 겹치는 조상이 나올 때 까지 반복
    while list(set(n1_ancestors).intersection(n2_ancestors)) == []:
        p = node_info[n1]
        n1_ancestors.append(p) #[16, 10, 4]
        n1 = p
        
        p = node_info[n2]
        n2_ancestors.append(p) # [7, 6, 4]
        n2 = p
        
    
    result = set(n1_ancestors).intersection(n2_ancestors) # {4}
    print("".join(map(str,result))) # 4 



"""
#시간초과

T = int(input());


# 자식 : 부모 형식으로 딕셔너리 바꿈
# {(14, 13): 1, (5, 4, 1): 8, (16, 11, 2): 10, (9,): 5, (6, 10): 4, (15, 7): 6, (3, 12): 16}
def reverse(item):
    key, value = item
    return tuple(value),key

for i in range(T):
    N = int(input())
    node_info = dict()

    # 부모 : 자식들 형식으로 딕셔너리 생성
    #{1: [14, 13], 8: [5, 4, 1], 10: [16, 11, 2], 5: [9], 4: [6, 10], 6: [15, 7], 16: [3, 12]}
    for i in range(N-1):
        parent, child = map(int,input().split())

        if parent in node_info:
            node_info[parent].append(child)
        else:
            node_info[parent] = [child]

    node_info = dict(map(reverse , node_info.items()))
   
    n1, n2 = map(int,input().split())
    n1_ancestors, n2_ancestors = [n1],[n2]
    

    while list(set(n1_ancestors).intersection(n2_ancestors)) == []:
        for key,value in node_info.items():
            if n1 in key:
                n1_ancestors.append(value)
                n1 = value
                break;

            if n2 in key:
                n2_ancestors.append(value)
                n2 = value
                break;

    #print(node_info)
    #print(n1_ancestors)
    #print(n2_ancestors)
    result = set(n1_ancestors).intersection(n2_ancestors)
    print("".join(map(str,result)))
"""

        
            
            

    
        
