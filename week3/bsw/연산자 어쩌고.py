N = int(input())
numbers = list(map(int, input().split()))

# + - x //
cnt_signs = list(map(int, input().split()))

signs=[]

for _ in range(cnt_signs[0]):
    signs.append('+')
for _ in range(cnt_signs[1]):
    signs.append('-')
for _ in range(cnt_signs[2]):
    signs.append('*')
for _ in range(cnt_signs[3]):
    signs.append('//')


from itertools import permutations

permutations_signs = list(set(permutations(signs, len(signs))))

print(permutations_signs)

max_num = -1e9
min_num = 1e9

for perms in permutations_signs:
    result=numbers[0]
    for i in range(1, len(numbers)):
        if perms[i-1] == '+':
            result+=numbers[i]
        elif perms[i-1] == '-':
            result-=numbers[i]
        elif perms[i-1] == '*':
            result*=numbers[i]
        elif perms[i-1] == '//':
            if result >= 0:
                result//=numbers[i]
            elif result < 0:
                result = -(abs(result)//numbers[i])
        
    max_num = max(max_num, result)
    min_num = min(min_num, result)
    
print(max_num, min_num)