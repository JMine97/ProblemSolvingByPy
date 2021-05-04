'''
O(n)

1차 시도 : C# 같이 # 붙은 친구들은 한 문자로 인식시키기 위해 다른 문자로 바꿔줘야 함 ex)C#->c(소문자)
2차 시도 : return "(None)" 주의
3차 시도 : 분만 고려하지 말고 시간도 고려해줘야 함
4차 시도 : arr 정렬할 때 그냥 정렬하면 오름차순으로 길이가 짧은 게 먼저 나옴, reverse=True 붙여주기

성공!
'''

def changenote(note):
    note=note.replace('C#','c')
    note=note.replace('D#','d')
    note=note.replace('F#','f')
    note=note.replace('G#','g')
    note=note.replace('A#','a')
    return note

def solution(m, musicinfos):
    arr=[] #[제목, 음표]
    m=changenote(m)

    for mm in musicinfos:
        mm=mm.split(',')
        end, start=mm[1], mm[0]
        title, sound=mm[2],changenote(mm[3])
        end_hour, start_hour=int(mm[1].split(':')[0]), int(mm[0].split(':')[0])
        end_min, start_min=int(mm[1].split(':')[1]), int(mm[0].split(':')[1])
        length=(end_hour-start_hour)*60+(end_min-start_min)

        #길이 맞추기
        sound = sound*(length//len(sound))+sound[:length%len(sound)]
        arr.append([title, sound])
    
    arr.sort(key=lambda x:len(x[1]), reverse=True)
    
    for i in arr:
        if m in i[1]:
            return i[0]
        
    return "(None)"
