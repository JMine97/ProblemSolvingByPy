from queue import Queue

def solution(N):
    q = Queue()
    decrease_num_count = -1

    # 만들 수 있는 감수하는 숫자 최대 개수가 1023개이기 때문에 초과 하면 -1리턴
    if N >= 1023:
        return -1

    if N == 0:
        return 0

    #0~9 까지는 무조건 감소하는 숫자
    for i in range(10):
        q.put(i)
        decrease_num_count += 1
        
        if i == N:
            return i
        

    #맨 뒷자리 숫자보다 작은 수를 붙여가면서 순서 계산
    while not q.qsize() == 0:
        num = q.get()
        last_num = num%10 #마지막 자리 숫자 가져오기
        for i in range(last_num):
            q.put(num*10 + i)
            decrease_num_count += 1
          
            if decrease_num_count == N:
                return num*10 + i

N = int(input())
print(solution(N))


#한 개를 가지고 다음 거 만들어서 쭉
