# 알고리즘 : 정렬 2
2020.02.02
병합정렬, 퀵정렬

## 병합 정렬(Merge Sort)
![병합정렬 그림](https://i.imgur.com/ood27RZ.png)
1. 입력을 반으로 나누고 
2. 나눈 전반부와 후반부를 각각 독립적으로 정렬함. 
3. 마지막으로 정렬된 두 부분을 합쳐서, 병합해서 정렬된 배열을 얻음

전반부/후반부를 정렬할 때도 역시 반으로 나눈 다음 정렬에서 병합  
자신에 비해 크기가 반인 문제를 두개 푼다음 이들을 병합하는 일을 재귀적으로 반복  

### 동작

```python
def merge(left, right):
    result = []
    # left, right요소 하나도 없을때까지 반복
    while len(left) > 0 or len(right) > 0:
        # 둘 다 1개보다 많으면 두쪽의 가장 작은 값부터 비교 시작(정렬되었다는 가정)
        if len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                result.append(left[0])
                # 큰값 발견하면 하나씩 result에 넣게 되고 작은 값 없앰
                left = left[1:]
            else:
                result.append(right[0])
                right = right[1:]
        # 한쪽이 result 리스트에 다 들어갔다면 다른 한쪽에서 작은값부터 차례로 append
        elif len(left) > 0:
            result.append(left[0])
            left = left[1:]
        elif len(right) > 0:
            result.append(right[0])
            right = right[1:]
    return result

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_arr = arr[:mid]
    right_arr = arr[mid:]
    left_arr = merge_sort(left_arr)
    right_arr = merge_sort(right_arr)
    # 재귀 - 왼배열과 오른배열을 나눌 수 있을 때까지 나눈다(1개 남을때까지)
    return merge(left_arr, right_arr)
    # merge로 정렬하면서 병합한다
```
### 수행시간
데이터의 개수가 n이고, 이를 정렬하는데 cn이라는 시간이 걸린다 가정(c는 임의의 상수 - 정렬하고 병합하는데는 선형시간이 필요: 리스트 안의 값 하나하나를 다 보기 때문에)  
전체 층의 개수는 항상 log n이 된다(데이터 개수가 8개이면 전체 층의 개수는 3층)  
상수항(c)를 무시하고 생각해보면 계산복잡성은 `O(nlogn)`(각 층의 계산시간 * 전체 층의 개수)  
2개가 아니라 a개로 쪼갤 경우도 층의 수는 loga n이 되는데 이는 로그의 성질에 의해 log2 3 * log2 n과 같음 따라서 이 경우에도 `O(nlogn)`

## 퀵 정렬(Quick Sort)
평균적으로 가장 좋은 성능을 가져 현장에서 가장 많이 쓰는 알고리즘  
1. 한 원소를 기준원소로 잡고, 이보다 작은 원소들은 왼쪽에, 나머지 원소들은 오른쪽에 오도록 재배치
2. 왼쪽 원소와 오른쪽 원소를 독립적으로 정렬, 이때 기준원소는 영향을 받지 않고 그대로 있음
3. 이때 기준 원소는 왼쪽과 오른쪽의 정렬을 시작하기 전에 이미 제자리를 찾은 것으로, 왼쪽 오른쪽 정렬이 끝나는 순간 전체 배열의 정렬이 끝남

### 동작
맨 뒤의 원소를 기준원소로 삼는 것으로 가정하고 구현  
재귀함수가 쓰이는데, 왼쪽 오른쪽 부분 배열 정렬할때도 퀵 정렬을 재귀적으로 사용한다  
병합 정렬이 먼저 재귀적으로 작은 문제를 해결한 후 후처리를 하는 반면  
퀵 정렬은 선행 작업을 한 다음 재귀적으로 작은 문제를 해결하면서 끝냄
```python
#뭔가 되게 우아하다;
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[-1]
    lesser_arr, equal_arr, greater_arr = [], [], []
    for num in arr:
        if num < pivot:
            lesser_arr.append(num)
        elif num > pivot:
            greater_arr.append(num)
        else:
            equal_arr.append(num)
    return quick_sort(lesser_arr) + equal_arr + quick_sort(greater_arr)

# 리스트 컴프리헨션 이용
def quick_sort(ARRAY):
    ARRAY_LENGTH = len(ARRAY)
    if( ARRAY_LENGTH <= 1):
        return ARRAY
    else:
        PIVOT = ARRAY[-1]
        GREATER = [ element for element in ARRAY[:-2] if element > PIVOT ]
        LESSER = [ element for element in ARRAY[:-2] if element <= PIVOT ]
        return quick_sort(LESSER) + [PIVOT] + quick_sort(GREATER)
```

### 수행시간
우선 분할하는 건 배열을 왼쪽부터 끝까지 한 번 훑으므로 O(n)
최적의 경우 : 분할이 항상 반반씩 균등하게 될 때, 병합 정렬과 거의 같아짐 O(nlogn)  
최악의 경우 : 계속해서 한쪽은 하나도 없고 다른 쪽에 다 몰리도록 분할이 되는 경우 O(n^2) - 거꾸로 되어있어서 다 하나씩 선형적으로 보면서 뒤집어야 하는 경우  

한쪽이 완전히 비거나 이에 근접한 상태가 반복되면 이런 비효율적인 시간이 나옴  

증) 퀵정렬의 평균적인 수행시간  
기준원소가 n개의 원소 중 작은 순서로 몇등인지에 따라 분할 모양 결정  
기준원소가 1등일 경우 왼쪽:오른쪽 = 0 : n-1  
기준원소가 2등일 경우 왼쪽:오른쪽 = 1 : n-2  
기준원소가 i등일 경우 왼쪽:오른쪽 = i-1 : n-1  
이경우 수행시간은 `T(n) = T(i-1) + T(n-1) + O(n)`  

기준원소는 동일한 확률로 1등부터 n등 중의 하나가 되므로 이들을 평균내면 `O(nlogn)`