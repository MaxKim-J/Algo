'''
백준 6603번 로또

itertools.combination 쓰면 푸는데 오분도 안걸리겠지만... 탐색으로 풀자

- 연산 횟수
    - kC6 경우의 수를 모두 구하는 것이므로 백트랙킹으로 경우의 수를 만들 수 있을 것
    - 최악 입력은 12개 => 12개로 조합
    - 12 -> 1~11합 -> 1~10합 -> 1~9합 ... 이런식으로 인덱스의 범위를 줄여 순회하는 꼴이 됨
    - 그럼 recursion maximum만 맞추면 대충 o(n) 이하로 끝날 수 있음(k가 적어서 거의 상수시간일것)
'''


def solve(enable, target):
    if 6 - len(target) > len(enable):
        return
    if len(target) == 6:
        result.append(target)
        return
    for i, num in enumerate(enable):
        solve(enable[i+1:], target + [num])


while True:
    k, *nums = input().split()
    if k == '0':
        break
    result = []
    solve(nums, [])
    for str in result:
        print(' '.join(str))
    print()
