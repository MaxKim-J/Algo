# 백준 10250 acm호텔
# https://www.acmicpc.net/problem/10250
# 시간 : 30분
# 경과 : 틀렸습니다 - 맞았습니다 

data_num = int(input());

for _ in range(data_num):
    H, W, N = map(int, input().split())
    room_height = (N-1)%H + 1
    room_num  = ((N-1)//H) + 1
    print(room_height*100 + room_num)

#! 처음에 틀렸습니다 뜬 이유 : 테스트 케이스는 맞았는데 대충 다른 예시도 맞을 것 같아서
#* 배운점 : 디버깅을 좀 빡세개 하자 더 집중! 특히 나머지, 몫 사이클일때는 변곡점일때 값 변하는지 잘 봐야댐
#? W는 낚시값이었음(맞나?)