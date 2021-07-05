T = int(input())

for _ in range(T):

    N = int(input())

    tree = {}
    for _ in range(N-1):
        parent, child = map(int, input().split())
        tree[child] = parent

    all_nodes = set([i for i in range(1,N+1)])
    children = set(i for i in tree.keys())
    root = (all_nodes-children).pop()
    
    tree[root] = -1

    node1, node2 = map(int, input().split())

    answers=[]
    for cur in [node1, node2]:
        visited=[]

        while cur in tree.keys():
            visited.append(cur)
            cur = tree[cur]
        
        answers.append(visited)
    # print(tree)
    # print(answers)
    visited1, visited2 = answers[0], answers[1]
    
    short = len(set(visited1) & set(visited2))

    print(visited1[-short])
    '''
      2
     3 
    1 4
    5
    '''