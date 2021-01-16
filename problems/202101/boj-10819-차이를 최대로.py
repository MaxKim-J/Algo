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

# itertools.permutations로 모든 곱 경우의수 구하면 좀더 빨라짐
'''
변태 풀이

def next_permutation(a):
    i = len(a)-1
    while i > 0 and a[i-1] >= a[i]:
        i -= 1
    if i <= 0:
        return False
    j = len(a)-1
    while j >= i and a[j] <= a[i-1]:
        j -= 1

    a[i-1],a[j] = a[j],a[i-1]

    j = len(a)-1
    while i < j:
        a[i],a[j] = a[j],a[i]
        i += 1
        j -= 1

    return True

def calc(a):
    ans=0
    for i in range(1, len(a)):
        ans += abs(a[i]-a[i-1])
    return ans

n = int(input())
a = list(map(int,input().split()))
a.sort()
ans = 0
while True:
    temp = calc(a)
    ans = max(ans, temp)
    if not next_permutation(a):
        break
print(ans)
'''
