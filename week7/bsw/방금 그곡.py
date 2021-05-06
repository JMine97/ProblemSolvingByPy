# def hash(m):
#     chg_m = ''
#     for i in range(len(m)):
#         piece = m[i:i+2]
#         if m[i] == '#':
#             continue
#         elif piece == 'C#':
#             chg_m += 'H'
#         elif piece == 'D#':
#             chg_m += 'I'
#         elif piece == 'F#':
#             chg_m += 'J'
#         elif piece == 'G#':
#             chg_m += 'K'
#         elif piece == 'A#':
#             chg_m += 'L'
#         else:
#             chg_m += m[i]
#     return chg_m


# replace는 문자열 전체를 처리한다
# find와 다름
def hash(m):
    m = m.replace('C#', 'H')
    m = m.replace('D#', 'I')
    m = m.replace('F#', 'J')
    m = m.replace('G#', 'K')
    m = m.replace('A#', 'L')
    return m


def solution(m, musicinfos):
    answer = ''
    
    chg_m = hash(m)
    dic = {}
    
    for musicinfo in musicinfos:
        start_time, end_time, name, sheet = musicinfo.split(',')
        
        sheet = hash(sheet)
        a, b = start_time.split(':')
        c, d = end_time.split(':')
        time = (int(c) - int(a)) * 60 + (int(d) - int(b))
        
        chg_sheet = ''
        for i in range(time):
            if i >= len(sheet):
                i = i % len(sheet)
            chg_sheet += sheet[i]
        
        dic[name] = chg_sheet
    
    for key in dic.keys():
        if chg_m in dic[key]:
            if answer:
                # 조건이 일치하는 음악이 여러개일 때
                if len(dic[answer]) < len(dic[key]):
                    answer = key    
            else:
                answer = key
            
    if not answer:
        answer += "(None)"
    
    return answer
# A B C D E F G H  I  J  K  L
#               C# D# F# G# A#