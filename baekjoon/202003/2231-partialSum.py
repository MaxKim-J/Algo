# 백준 2231번 부분합
# https://www.acmicpc.net/problem/2231
# 시간 : 50분
# 경과 : 런타임 에러 - 맞았습니다


def partial_sum(num):
    num_len = len(str(num))
    start = num if num < num_len*9 else num_len*9
    for count in range(start, 0, -1):
        eval_num = num - count
        figure_sum = 0
        for n in str(eval_num):
            figure_sum += int(n)
        if figure_sum == count:
            return eval_num
    return 0


N = int(input())
print(partial_sum(N))

#! 런타임에러 나온 이유 : 예외처리 못해서, num_len*9보다 낮은 값들 처리 어캐해야할지 생각해야 했다
# * 충분히 노트에서 테스트를 해봐야 함
