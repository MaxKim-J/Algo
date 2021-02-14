# 선택 
2020.02.11

## 선형시간 선택 
### 구현
퀵소트의 방법을 사용한다
```python
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
  # partition이 리턴한 위치는 배열에서 몇번째로 작은지 알려주게 됨
  howSmall = found - start + 1
  # 왼쪽에서만 고려
  if i < howSmall:
    select(arr, start, found-1, i)
  # 딱 찾았을때 리턴
  elif i==howSmall:
    return arr[found]
  # 오른쪽에서만 고려
  else:
    return select(arr, found+1, end, i-howSmall)
```
### 수행시간
**직관적으로는**
퀵소트의 경우에는 중간이 되는 기준 원소를 하나 꺼내서  
좌우로 정렬하는 과정을 거치니 O(nlogn)이지만  
이경우에는 선택만(partition)만 하니까 O(n)=선형시간이 걸림  
하지만 최악의 경우에는 퀵소트처럼 분할이 불균일할 경우 O(n^2)가 된다  

## 최악의 경우에도 선형시간인 선택
배열 그룹의 중앙값을 이용해서 파티션을 함  
최악의 경우에 가까워질수록 살펴봐야할 왼/오 파티션의 크기를 이차원적으로 줄이는 아이디어    

### 구현
```python
def partition(arr, start, end):
    pivot = arr[end]
    i = start-1
    for j in range(start, end):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[end] = arr[end], arr[i+1]
    return i+1

# 메소드로 직접짜봄, 일단 재귀 안쓰구 짜봄
def linearSelect(arr, start, end, i):
    # 1
    if len(arr) <= 5:
      return arr[i]
    whole_arr, medium_arr = [], []
    # 2
    for num in range(0, end+1, 5):
        whole_arr.append(arr[num:num + 5])
    # 3
    for part in whole_arr:
        med = sorted(arr)[len(arr) // 2]
        medium_arr.append(med)
    # 4
    selected = sorted(medium_arr)[len(medium_arr) // 2]
    # 5
    found = partition(arr, start, end)
    # 6
    howSmall = found - start + 1
    if i < howSmall:
        return linearSelect(arr, start, found - 1, i)
    elif i == howSmall:
        return arr[found]
    else:
        return linearSelect(arr, found+1, end, i-howSmall)
```

### 수행시간
최악의 경우에도 O(n)이 걸림  
책에있는거 대충 이해;;
