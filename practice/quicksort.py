import time
import random
start = time.time()


def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        for j in range(i):
            if arr[i] < arr[j]:
                ins_value = arr[i+1]
                arr.insert(j+1, ins_value)
                del arr[i+1]
    return arr


a = [i * random.randint(0, 1000) for i in range(50000)]
print(insertion_sort(a))
print("time :", time.time() - start)
