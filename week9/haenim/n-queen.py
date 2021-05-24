"""
o(n)
"""

n = int(input())
count = 0
row, left, right = [0 for _ in range(n)],  [0 for _ in range(2*n-1)], [0 for _ in range(2*n-1)]

def solution(index):
    if index = n: 
        count += 1
        return

    for col in range(n): 
        if row[col] + left[index+col] + right[n-1 + index - col] == 0 :
            row[col] = left[index+col] = right[n-1+index-col]=1
            solution(index+1)
            row[col] = left[index+col] = rigth[n-1+index-col] = 0

solution(0)
print(count)
