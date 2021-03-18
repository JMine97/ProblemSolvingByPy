def sol(N):
    q = [i for i in range(10)]
    arr = [i for i in range(10)] #감소하는 수들의 list

    while(q):
        num=q.pop(0)
        cnt = num%10
        if cnt != 0:
            for i in range(cnt):
                q.append(num * 10 + i)
                arr.append(num * 10 + i)
    arr.sort()
    
    if N >= len(arr): # 0번째가 존재하므로 
        print(-1)
    else:
        print(arr[N])


sol(int(input()))


'''
감소하는 수의 최대 수는 9876543210 -> 총 개수 자체가 많지 않을 것 -> 전부 구해서 리스트에 담아 N번째 수를 출력
1. 큐의 숫자를 pop해 일의자리 체크
2. 체크한 숫자 보다 작은 수가 있을경우 뒤에 붙여주고 q.append / arr.append
3. 큐가 빌때까지 반복
4. arr.sort
5. N 번째 수 출력 (0번째 수가 존재하므로 N-1을 하지 않는다)
'''

