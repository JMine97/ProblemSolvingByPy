def change(m):
    if 'A#' in m: m = m.replace('A#', 'a')
    if 'C#' in m: m = m.replace('C#', 'c')
    if 'D#' in m: m = m.replace('D#', 'd')
    if 'F#' in m: m = m.replace('F#', 'f')
    if 'G#' in m: m = m.replace('G#', 'g')
    return m

def solution(m, musicinfos):
    m = change(m)
    answer = []
    for music in musicinfos:
        start, end, name, line = music.split(',')
        start_h, start_m = map(int, start.split(':'))
        end_h, end_m = map(int, end.split(':'))
        
        runtime = (end_h-start_h)*60 + (end_m-start_m) 
        line = change(line) # 
        
        realtime = (line*3)
        print(realtime)
        
        answer.append((realtime, name))
        
    answer.sort(key=lambda x : len(x[0]), reverse=True) # 조건 : 제일 긴 음악을 반환, 재생시간이 같으면 먼저 입력된 음악 반환
      
    for ans in answer:
        if m in ans[0]:
            return ans[1]
    return "(None)"
