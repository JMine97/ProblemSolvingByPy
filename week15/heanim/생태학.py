
tree_dict = dict()
total = 0

while 1:
    tree = input().rstrip()
    if not tree:
        break

    total += 1
    
    if tree not in tree_dict.keys():
        tree_dict[tree] = 1
    else :
        tree_dict[tree] += 1

lst = sorted(list(tree_dict.keys()))

for tree in lst:
    print(tree," ",round(tree_dict[tree]/total *100,4))
