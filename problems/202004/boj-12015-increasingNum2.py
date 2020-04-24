# 백준 12015 : 가장 긴 증가하는 부분 수열2
# https://www.acmicpc.net/problem/12015
# 시간 : 40분
# 경과 : 맞았습니다(548ms-pypy3)


N = 6
num_list = [10, 20, 10, 30, 20, 50]
inc = []


for num in num_list:
    start, end = 0, len(inc)
    answer = end
    while (start <= end):
        mid = (start+end)//2
        if mid >= len(inc):
            answer = mid
            break
        if inc[mid] >= num:
            answer = mid
            end = mid-1
        else:
            start = mid+1

    print(answer)
    if len(inc) <= answer:
        inc.append(num)
    else:
        inc[answer] = num

print(len(inc))

# * 접근 1) 좀 해맸었는데 생각보다 이분탐색을 간단하게 적용하면 됐다
# * 접근 2) 수열 배열을 따로 만들고, 이분탐색으로 수열 배열에 있는 기존 수를 찾아 인덱스를 반환하거나
#! 접근 3) 큰 수가 나타나 미드가 갯수보다 올라가서 리스트 밖에서 값을 찾아야 하는 시점이 되면 그 값을 answer로 삼게 된다(혹은 len(inc)+1)
# * 접근 4) 이분탐색으로 얻은 인덱스를 바탕으로 그 값이 수열 배열의 크기보다 크다면 맨 뒤에 원소 추가
#! 접근 5) 그렇지 않다면 수를 바꿔준다 => 이래야 딱 증가하는 오름차순대로 배열에 들어감

# * 만약에 20이 수열 배열에 들어가있는 상태에서 그 다음 인덱스에서 30이 나왔는데 그 다음이 25일 경우 30은 폐기되고 25가 들어간다
# * 증가수열의 관점에서 30에서 25로 떨어질 수 없고, 그 다음부터는 25보다 높은 수가 나오면 이는 또 증가수열을 이어나갈 수 있기 때문에
