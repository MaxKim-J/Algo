# 얘는 그냥 개빠른 BFS같기도 함
num = int(input())
count, temp = 0, [num]

while (1 not in temp):
    dp = set()
    #! 배열 하나를 계속 재사용 하는 방법은 대충 맞긔
    # 매번 해제되고 매번 다시 순회 => 매번 3개 이하의 숫자를 넣고 그거로 다시 순회
    # 최대 한 루프에 3번씩 순회
    # 같은 숫자가 2개 들어있지는 않음 => 2개 이상 평가할 필요는 없음
    # 1이 나올때까지만 반복하면 됨
    for n in temp:
        if n % 3 == 0:
            dp.add(n // 3)
        if n % 2 == 0:
            dp.add(n // 2)
        dp.add(n-1)
    count += 1
    temp = list(dp.copy())
print(count)
