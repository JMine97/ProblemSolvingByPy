# 5052번_전화번호 목록
'''
전화번호 목록 일관성 check 프로그램
일관성 : 한 번호가 다른 번호의 접두어인 경우가 없어야 한다.

복잡도 : O(n) 
'''
import sys
input = sys.stdin.readline

def testCase(N):
    phone = []
    for _ in range(N):
        temp = input().rstrip('\n')
        phone.append(temp)
    phone.sort()
    #print(phone)
    # 옆에 있는 전화번호만 확인하면 된다는 것을 어떻게 생각해내나요..?ㅠ
    for i in range(len(phone)-1):
        if phone[i] in phone[i+1][:len(phone[i])]:
            return 'NO'
    return 'YES'

t = int(input())
for _ in range(t):
    n = int(input())
    print(testCase(n))
    

################################ 시간 초과 코드 ###############################
# 이중 포문을 쓸 경우 시간 초과!
import sys
input = sys.stdin.readline

t = int(input())

def testCase(N):
    phone = []
    for _ in range(N):
        temp = input().rstrip('\n')
        phone.append(temp)

    phone = sorted(phone, key=lambda x: len(x))

    for i in range(N-1):
        for j in range(i+1, N):
            if phone[i] == phone[j][:len(phone[i])]:
                if len(phone[i]) != len(phone[j]):
                    return 'NO'
    return 'YES'
for _ in range(t):
    n = int(input())
    print(testCase(n))
