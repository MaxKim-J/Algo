# 백준 1018번 체스판 칠하기
# https://www.acmicpc.net/problem/1018
# 시간 : 1시간 => 1시간 오기가 생겨서 좀더 고민하다 결국 못품
# 경과 : 못 품


def check_BW(ex):
    # wbwbwb... 일때
    cnt1 = 0
    for i in range(8):
        for j in range(8):
            i_ = (0 if i in [0, 2, 4, 6] else 1)
            j_ = (0 if j in [0, 2, 4, 6] else 1)
            # 0,0/0,2 등 짝수 === B가 들어갈 자리
            if (i_ == 0 and j_ == 0) or (i_ == 1 and j_ == 1):
                if ex[i][j] != "B":
                    cnt1 += 1
            # 0,1/0,3 등 홀수 === W가 들어갈 자리
            if (i_ == 0 and j_ == 1) or (i_ == 1 and j_ == 0):
                if ex[i][j] != "W":
                    cnt1 += 1
    # bwbwbw... 일때
    cnt2 = 0
    for i in range(8):
        for j in range(8):
            i_ = (0 if i in [0, 2, 4, 6] else 1)
            j_ = (0 if j in [0, 2, 4, 6] else 1)
            # 0,0/0,2 등 짝수 === W가 들어갈 자리
            if (i_ == 0 and j_ == 0) or (i_ == 1 and j_ == 1):
                if ex[i][j] != "W":
                    cnt2 += 1
            # 0,1/0,3 등 홀수 === B가 들어갈 자리
            if (i_ == 0 and j_ == 1) or (i_ == 1 and j_ == 0):
                if ex[i][j] != "B":
                    cnt2 += 1

    return min(cnt1, cnt2)


n, m = map(int, input().split())
# 이차원 배열 사용
s = [list(input()) for i in range(n)]
check = []

# 8*8이 되는 모든 경우의 이차원배열을 잘라서 함수에 넣기
for i in range(n-7):
    for j in range(m-7):
        ex = [z[(0+j):(8+j)] for z in s[(0+i):(8+i)]]
        check.append(check_BW(ex))
print(min(check))


#! 못푼이유 1) 처음에 문제 이해를 잘 못해서 8*8부분을 못보고 그냥 전체를 체스판으로 만드는 경우의 수를 계산했음(반성하자;;)
#! 못푼이유 2) 결국 경우를 나눠서 계속 봐야한다는 생각은 했지만 실행에 옮기지 못함
# * 이차원 배열 쓰는게 코드가 제일 깔끔하다는 생각을 했어야댐...객기부리지 말구,,,2차원 배열을 왜 그렇게 쓰기 싫었는지,,,
# * 문제를 풀면서 문자열로 합친 후 8*8 경우를 모두 도는 for 문을 만들었다,, 뭔가 한번 해보고 싶었음,,
# * 사실 인덱스가 이렇게 복잡하면 풀이가 삼천포로 가고 있다는 생각을 했었어야 함,,,뭔가 한번 해보고 싶어서 하면 안되구 당위성을 가지고 움직이자
"""
height, width = map(int, input().split())

test1 = ["BBBBBBBBWBWBW", "BBBBBBBBBWBWB", "BBBBBBBBWBWBW", "BBBBBBBBBWBWB", "BBBBBBBBWBWBW",
         "BBBBBBBBBWBWB", "BBBBBBBBWBWBW", "BBBBBBBBBWBWB", "WWWWWWWWWWBWB", "WWWWWWWWWWBWB"]

whole_board = ""

for row in test1:
    whole_board += row

result = []
for j in range(width-8+1):
    for n in range(height-8+1):
        B_count, W_count = 0, 0
        for i in range(n*13+j, n*13+(width*7)+j+1, 13):
            print(whole_board[i:i+8])
            B_count += whole_board[i:i+8].count("B")
            W_count += whole_board[i:i+8].count("W")
        bigger = B_count if B_count > W_count else W_count
        re_paint = bigger - 32
        result.append(re_paint)
print(result)
print(min(result))
"""
