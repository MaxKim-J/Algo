N = int(input())
arr = list(map(int, input().split()))

max_num = -8000


def calculate(N, arr):
    result = 0
    for i in range(N - 1):
        result += abs(arr[i] - arr[i+1])
    return result


def recursion(target, resource):
    global N, max_num
    if len(target) == N:
        cal_result = calculate(N, target)
        if cal_result > max_num:
            max_num = cal_result
            return
    for i in resource:
        new_target = target[:]
        new_target.append(i)
        new_resource = resource[:]
        new_resource.remove(i)
        recursion(new_target, new_resource)


recursion([], arr)
print(max_num)
