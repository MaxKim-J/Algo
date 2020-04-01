# 백준 7568번 덩치
# https://www.acmicpc.net/problem/7568
# 시간 : 26분
# 경과 : 맞았습니다(60ms)


data_num = int(input())

result = []
fig_arr = []

for i in range(data_num):
    figure = tuple(map(int, input().split()))
    fig_arr.append(figure)

for fig in fig_arr:
    count = 1
    new_arr = list(filter(lambda x: x != fig, fig_arr))
    for fig_comp in new_arr:
        if fig[0] < fig_comp[0] and fig[1] < fig_comp[1]:
            count += 1
    result.append(str(count))

print(" ".join(result))

# ? 최적화의 가능성이 보이는데,,,
#! 접근) 자기 자신과 비교하는 과정이 있는데 쓸데없는 반복임. 개선할 가능성이 있긴 있는데 근데 코드가 넘 복잡해짐
# * 근데 그렇게 개선해도 걸리는 시간은 똑같넹(쓸데없었다고 한다)

#! 배운점) 리스트의 remove 메소드는 어떤 값을 제거?
