enable = {str(x) for x in range(10)}

N = int(input())
missing_button_num = int(input())
if(missing_button_num != 0):
    missing_buttons = set(input().split())
    enable -= missing_buttons

result = abs(N - 100)

for i in range(1000001):
    is_valid = True
    for num in str(i):
        if(num not in enable):
            is_valid = False
            break
    if(is_valid):
        result = min(result, abs(N - i) + len(str(i)))

print(result)

# 재귀를 이용해서 모두 트래킹하는 백트랙킹만 있는게 아니라
# 매우 많은 값을 순회하는 백트랙킹도 있다
# 하지만 파이썬은 1초에 20000000번이니까 백만번정도는 1초안에 돌리므로 가능
# 채널의 최댓값이 오십만이므로 그 밑의 숫자들은 다돌아야되고

'''
매우 번거롭지만 빠른 내풀이;;

target = int(input())
missing_N = int(input())
enable = {i for i in range(10)}

if missing_N == 0:
    enable = list(enable)
else:
    missing_buttons = {*map(int, input().split(' '))}
    enable = list(enable - missing_buttons)

push_count = 0


def find_nearlest_number(target, enable):
    global push_count
    result = ''
    for i in target:
        min_abs = 10
        min_abs_number = 0
        for j in enable:
            new_abs = abs(int(i) - j)
            if new_abs < min_abs:
                min_abs = new_abs
                min_abs_number = j
        if (result == '' and min_abs_number == 0):
            if len(enable) > 1:
                result += str(enable[1])
            else:
                return 10000001
        else:
            result += str(min_abs_number)
        push_count += 1
    return int(result)


nearlest_number = find_nearlest_number(str(target), enable)
numeric_button_push = abs(target - nearlest_number) + push_count
up_down_button_push = abs(target-100)

print(min(numeric_button_push, up_down_button_push))
'''
