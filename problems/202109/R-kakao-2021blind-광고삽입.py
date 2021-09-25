'''
저번의 구간 문제와는 양상이 다른 문제였다. 완전탐색으로 풀다가 시간초과됨
logs배열의 크기가 30만이라는 거 보고, 완전탐색으로 풀면 O(n^3)이 대충 되는데 그러면 완전탐색은 안된다는 감을 잡아야 했음
큰 타임라인을 하나 구현하고, 매초를 배열로 삼아서 그 초마다 몇명이 보고있는지를 모두 찾아 기록한후
시작점을 옮겨가며 광고 시간 내에 들어가는 사람이 얼마나 많은지 파악해야 했다 일종의 DP를 하는건데
그리고 처음 시작하는 시간(0)과 끝 시간에 대한 엣지케이스도 고려해야한다
여전히 명징한 해결책! 아니다 싶으면 빨리 생각 전환! 이 잘 안된다
꽤 유용한 스킬이다
'''

# 완전탐색
def my_solution(play_time, adv_time, logs):
    answer = []
    p_logs = []
    r_logs = []
    
    h,m,s = adv_time.split(':')
    p_adv_time = int(h) * 3600 + int(m) * 60 + int(s)
    
    for log in logs:
        range_result = []
        for part in log.split('-'):
            h,m,s = part.split(':')
            result = int(h) * 3600 + int(m) * 60 + int(s)
            range_result.append(result)
        p_logs += range_result
        r_logs.append(range_result)
            
    p_logs = [0] + sorted(p_logs)
    
    for start in p_logs:
        end = start + p_adv_time
        mid_points = [start] + list(filter(lambda x:start<x<end, p_logs)) + [end]
        whole_play_time = 0
        for i in range(len(mid_points)-1):
            part_play_time = mid_points[i+1] - mid_points[i]
            for range_start, range_end in r_logs:
                if range_start <= mid_points[i] and mid_points[i+1] <= range_end:
                    whole_play_time += part_play_time
                    
        answer.append((whole_play_time, start))
        
    
    answer = sorted(answer, key=lambda x:(-x[0], x[1]))
    
    hour = answer[0][1] // 3600
    minute = (answer[0][1] - hour*3600) // 60
    seconds = answer[0][1] - hour*3600 - minute*60
    time = list(map(lambda x: '0'+str(x) if x<10 else str(x), [hour, minute, seconds]))
    
    return ':'.join(time)

def str2sec(string):
    hour, min, sec = map(int, string.split(':'))
    return hour * 3600 + min * 60 + sec

def sec2str(seconds):
    string = ''
    hour = seconds // 3600
    seconds -= hour * 3600
    min = seconds // 60
    seconds -= min * 60
    return f"{str(hour).zfill(2)}:{str(min).zfill(2)}:{str(seconds).zfill(2)}"
    
def solution(play_time, adv_time, logs):
    
    #  전체 재생시간과 광고 재생 시간을 초 단위로 바꿔 준다.
    play_time = str2sec(play_time)
    adv_time = str2sec(adv_time)
    
    # timeline[i]는 i초에서 몇명의 사람들이 보고 있는지
    timeline = [0] *(play_time+1)
    
    #logs를 돌면서 timeline의 시작시간에 +1 종료 시간에 -1을 해준다.
    #시작 시간에는 시청자 1, 종료 시간에 시청자 -1
    for log in logs:
        start, end= map(str2sec, log.split('-'))
        timeline[start] += 1
        timeline[end] -= 1
        
    #for문을 한번 돌면 비어있는 구간에 시청자 수를 알 수 있음
    for i in range(1, play_time+1):
        timeline[i] = timeline[i] + timeline[i-1]
        
    #* for문을 한번 "더" 돌면 timeline[0](0초) ~ timeline[i] 까지의 누적합이 된다.
    #누적합은 0 ~ i 초까지 누적 시청 시간이 된다.
    #이런식으로 하는 이유는 광고 시작 시간 A와 종료시간 B가 주어졌을 때
    #timeline[B] - timeline[A]로 더 빠르게 구할 수 있음 
    #! 이걸 안하면 구간의 시청자 수를 구할때 어디서부터 어디까지 구간의 모든 합을 더하고 -1 해줘야한다
    for i in range(1, play_time+1):
        timeline[i] = timeline[i] + timeline[i-1]
    
    answer = 0
    #0초에 광고를 시작했을때 누적 시간
    max_cnt = timeline[adv_time]
    
    for start in range(1, play_time):
        #광고 종료 시간이 영상 재생시간을 넘어가면 광고 재생 종료 시간을 영상 종료 시간(play_time)으로 둔다.
        end = play_time if start + adv_time >= play_time else start + adv_time 
        
        #시청자 수가 이전 답보다 많을 때를 찾으면서 값을 업데이트
        if max_cnt < timeline[end] - timeline[start]:
            max_cnt = timeline[end] - timeline[start]
            answer = start + 1
            #여기서 1초를 더해준 이유는 timeline[end] - timeline[start]가
            #start+1초 부터 end초사이의 누적 시간이기 때문에
            
    return sec2str(answer)
        