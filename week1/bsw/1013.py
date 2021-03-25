DFA = [[5,1], #0
       [2,9], #1
       [3,9], #2
       [3,4], #3
       [5,7], #4
       [9,6], #5
       [5,1], #6
       [8,7], #7
       [3,6], #8
       [9,9]] #9

T = int(input())

for _ in range(T):
    startNode = 0
    string = input()
    for i in range(len(string)):
        nextNode = DFA[startNode][int(string[i])]
        startNode = nextNode
        if nextNode == 9:
            break
    if nextNode == 4 or nextNode == 6 or nextNode == 7:
        print("YES")
    else:
        print("NO")


'''
유한 상태 기계
'''
