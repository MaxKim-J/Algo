def counting_sort(arr, K):
    c = [0] * K
    sorted_arr = [0] * len(arr)

    for i in arr:
        c[i] += 1

    for i in range(1, K):
        c[i] += c[i-1]

    for i in range(len(arr)):
        sorted_arr[c[arr[i]] - 1] = arr[i]
        c[arr[i]] -= 1

    return sorted_arr


def radix_sort(arr):
    # arr 배열중에서 maxValue를 잡아서 어느 digit, 자릿수까지 반복하면 될지를 정한다
    maxValue = max(arr)
    # 자릿수마다 countingSorting을 시작한다
    digit = 1
    while int(maxValue/digit) > 0:
        counting_sort(arr, digit)
        digit *= 10
    return arr


a = [1133, 2114, 4223, 1411, 5229, 1527, 6344, 1242, 2366, 1524, 8733]
print(radix_sort(a))
