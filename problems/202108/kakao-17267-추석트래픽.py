# range가 시작되거나 끝날때만 window 안에 들어가있는 구간의 개수가 바뀐다는 것 이용
def solution(lines):
    line_range=[]

    # 정수로 변환
    for l in lines:
        day, time, process = l.split(' ')
        hour, minute, seconds = time.split(':')
        process = str(float(process[:-1]))
        
        end = float(hour) * 3600 + float(minute) * 60 + float(seconds)
        start = end - float(process) + 0.001
        
        line_range.append((int(start*1000), int(end * 1000)))
        
    answer = []
    
    # 범위 2개를 가지고 겹치는지 확인
    length = len(lines)
    for i in range(length):
        s,e = line_range[i]
        p_range = [(s, s+999), (e, e+999)]
        
        for rs, re in p_range:
            count = 0
            for j in range(length):
                cs,ce = line_range[j]
                if (cs < rs and ce < rs) or (re < cs and re < ce):
                    continue
                count += 1
            answer.append(count)
    
    return max(answer)