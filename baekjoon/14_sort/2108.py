# 2108. 통계학
# 일단 쉽게 생각하자

from collections import Counter
import sys

# main
t = int(sys.stdin.readline())

numbers = []
for _ in range(t):
    numbers.append(int(sys.stdin.readline()))


def mean(nums):
    return round(sum(nums)/len(nums))


def median(nums):
    nums.sort()
    mid = nums[len(nums)//2]
    return mid


def mode(nums):
    mode_dict = Counter(nums)
    modes = mode_dict.most_common()
    if len(nums) > 1:
        if modes[0][1] == modes[1][1]:
            mod = modes[1][0]
        else:
            mod = modes[0][0]
    else:
        mod = modes[0][0]

    return mod


def scope(nums):
    return max(nums) - min(nums)


sys.stdout.write(
    f"{mean(numbers)}\n{median(numbers)}\n{mode(numbers)}\n{scope(numbers)}\n")
