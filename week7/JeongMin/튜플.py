'''
O(n)이라 생각
10^6으로 시간초과가 나지 않는다
'''

def solution(s): # s="{{2},{2,1},{2,1,3},{2,1,3,4}}"
    answer = []
    s = s.lstrip('{').rstrip('}').split('},{') #['2', '2,1', '2,1,3', '2,1,3,4']

    st = []
    for ss in s:
        st.append(list(map(int, ss.split(',')))) #[[2], [2, 1], [2, 1, 3], [2, 1, 3, 4]]
    st.sort(key=lambda x: len(x)) #길이로 정렬 #[[2], [2, 1], [2, 1, 3], [2, 1, 3, 4]]

    for i in st:
        for j in i:
            if j not in answer:
                answer.append(j)
    return answer #[2, 1, 3, 4]
