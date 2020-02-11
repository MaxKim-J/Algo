import time
import random


def partition(arr, start, end):
    pivot = arr[end]
    i = start-1
    for j in range(start, end):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[end] = arr[end], arr[i+1]
    return i+1


def select(arr, start, end, i):
    if len(arr) == 1:
        return arr[0]
    found = partition(arr, start, end)
    howSmall = found - start + 1
    if i < howSmall:
        return select(arr, start, found-1, i)
    elif i == howSmall:
        return arr[found]
    else:
        return select(arr, found+1, end, i-howSmall)


def linearSelect(arr, start, end, i):
    whole_arr, medium_arr = [], []
    for num in range(0, end+1, 5):
        whole_arr.append(arr[num:num + 5])
    for part in whole_arr:
        med = sorted(arr)[len(arr) // 2]
        medium_arr.append(med)
    selected = sorted(medium_arr)[len(medium_arr) // 2]
    found = partition(arr, start, end)
    howSmall = found - start + 1
    if i < howSmall:
        return linearSelect(arr, start, found - 1, i)
    elif i == howSmall:
        return arr[found]
    else:
        return linearSelect(arr, found+1, end, i-howSmall)


test_arr = [random.randint(-100, 100) for r in range(300000)]

select_start = time.time()
print(select(test_arr, 0, 10, 3))
print("select_time:", time.time() - select_start)
linearSelect_start = time.time()
print(linearSelect(test_arr, 0, 10, 3))
print("linearSelect_time:", time.time() - linearSelect_start)
