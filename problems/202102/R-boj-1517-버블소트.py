# 접근은 잘했는데 구현을 못한...
# 버블소트인데 병합정렬을 이용해야하는 희한함

# 얘는 신기하게도 공간 복잡도가 적은 안정정렬 병합정렬
# https://cantcoding.tistory.com/m/33


def merge_sort(start, end):
    global swap, arr
    size = end - start
    if size < 2:
        return arr

    mid = (start+end) // 2
    merge_sort(start, mid)
    merge_sort(mid, end)

    # 병합하는 과정에서 결국 자신보다 앞의 인덱스에서 큰 값의 숫자를 구하면 됨
    # 왼쪽 배열의 값이 새로운 배열에 추가되는 경우 - 오른쪽 리스트에서는 새로운 리스트로 먼저 채워진 왼쪽 리스트 원소의 개수만큼 스왑이 진행 => 이게 더 구현이 쉬움
    # 오른쪽 배열의 값이 새로운 배열에 추가되는 경우 - 왼쪽 리스트에서 새로운 리스트로 채워지지 않은 왼쪽 리스트의 원소의 개수만큼 스왑이 진행
    # 어느 한쪽 리스트를 기준으로 잡고 스왑을 계산
    merged_arr = []
    idx1, idx2 = start, mid
    count = 0
    while idx1 < mid and idx2 < end:
        # 오른배열
        if arr[idx1] > arr[idx2]:
            merged_arr.append(arr[idx2])
            idx2 += 1
            count += 1
        # 왼배열
        else:
            merged_arr.append(arr[idx1])
            idx1 += 1
            # 왼쪽 리스트에서 새로운 배열에 채워진 수만큼 스왑을 해야한다
            swap += count
    while idx1 < mid:
        merged_arr.append(arr[idx1])
        idx1 += 1
        swap += count
    while idx2 < mid:
        merged_arr.append(arr[idx2])
        idx2 += 1

    # arr 전체에 결과 반영하기(정렬이 된 것들에 한해)
    for t in range(len(merged_arr)):
        arr[start + t] = merged_arr[t]


n = int(input())
arr = list(map(int, input().split()))
swap = 0
merge_sort(0, n)
print(swap)
