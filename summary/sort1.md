# 알고리즘 : 정렬 1
2020.01.28  
선택/버블/삽입/힙  

출처: https://dataleaf.tistory.com/entry/Markdown에서-수식-입력하기 [정보의 잎사귀]

## 선택정렬(Selection Sort)
### 동작
배열에서 가장 큰 원소를 찾아 이 원소와 배열 끝자리에 있는 원소와 자리를 바꿈  
맨 뒷자리로 옮긴 원소는 자기 자리를 찾았으니 신경쓰지 않음  
정렬이 끝난 원소를 제외하고 나머지 원소들로 작업을 반복하면 됨  
마지막에 크기 2인 배열 A[1...2]의 두 원소중 가장 큰 원소를 A[2]에 넣고 나면 맨 앞 인덱스에 가장 작은수 자리잡음  

*가장 작은 수를 맨 앞 인덱스로 옮기는 방법으로도 구현 가능
```python
def selection_sort(arr):
  n = len(arr)
  for i in range(n-1 ,0, -1):
    max_idx = i
    for j in range(0, i):
        if arr[j] > arr[max_idx]:
          max_idx = j
    arr[i], arr[max_idx] = arr[max_idx], arr[i]
  return arr
```
### 수행시간
**모든 경우에 O(n^2)**  
- for 루프는 n-1번 순환 (n번 반복)
- max를 찾는 것은 부분 배열에서 가장 큰 수를 찾는 작업이므로 O(n)시간 소요
- 수를 비교하는 횟수가 알고리즘의 전체 시간을 좌우하므로 그렇게 생각해 보면 O(n^2)
```shell
# 수를 비교하는 횟수는 루프를 돌 때마다 1씩 줄어듦,, 1이 될때까지
(n-1) + (n-2) ... + 2 + 1 = n(n-1)/2
```
- 최악의 경우 : 모든 수가 정렬되어 있지 않은 경우, 두 원소 교환하는 일은 n-1번까지 발생
- 제일 좋은 경우 : 모든 수가 이미 정렬되어 있는 경우, 원소를 0회 교환함

## 버블 정렬(Bubble Sort)
### 동작
선택 정렬처럼 제일 큰 원소를 끝자리로 옮기는 작업을 반복하나, 제일 큰 원소를 오른쪽으로 옮기는 방법이 다르다  
선택 정렬은 그냥 max값을 찾아서 맨 끝 인덱스의 값과 바꾸지만, 버블정렬은 **옆의 있는 원소랑 계속 차레대로 비교해서 자리를 찾아가게 하는 식으로 바꾼다**
```python
def bubble_sort(arr):
  n = len(arr)
  for i in range(n-1, 0, -1):
    max_idx = i
    for j in range(0, i):
      # 옆의 원소만이랑 비교해서, 옆이 더 작으면 바꾼다
      # 옆이 더 크면 아무것도 안하고, 다음 인덱스로 넘어간다
      if arr[j+1] < arr[j]:
        arr[j+1], arr[j] = arr[j], arr[j+1]
  return arr
```
### 수행시간
**O(n^2)**
- 첫번째 for루프는 선택 정렬에서처럼 n-1번 순환한다
- 두번째 for루프는 last-1번 수행(last는 n에서 2가지 1씩 감소)(알고리즘 시간 좌우) 
- 원소 위치 바뀌는건 상수 시간에 수행 

**의미 없는 순환을 막으면** 제일 좋은 경우에 O(n)시간 걸리기도 함
```python
def bubble_sort(arr):
  n = len(arr)
  for i in range(n-1, 0, -1):
    max_idx = i
    # 원소 위치를 바꿨는지 여부를 검사하는 표식자
    is_sorted = True
    for j in range(0, i):
      if arr[j+1] < arr[j]:
        arr[j+1], arr[j] = arr[j], arr[j+1]
        is_sorted = False
    if is_sorted == True:
      print("이미 정렬된 배열이라구!")
      return
  return arr
```
이럴 경우 배열이 정렬된 상태로 입력되면, 버블 정렬은 for루프를 첫번째로 순환하고  
리턴하게 되어 O(n)시간 안에 끝난다

## 삽입정렬(Insertion Sort)
### 동작
이미 정렬되어있는 i개짜리 배열에 하나의 원소를 더하여 정렬된 i+1개짜리 배열을 만드는 과정을 반복함  
선택 정렬과 버블 정렬이 n개짜리 배열에서 시작하여 그 크기를 하나씩 줄이지만, **삽입 정렬은 한개짜리 배열에서 시작하여 그 크기를 하나씩 늘리는 정렬임**
```python
# 자료형 메소드를 쓰지 말자!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# 수도코드는 항상 특이한 메소드 없이도 만들 수 있게끔 나온다
# 메소드로 생각하지 말고, 값 비교하고, 바꾸고, 값 내리고, 올리고
# 자바로 하든 파이썬으로 하든 C로 푼다고, 총 칼 없이 돌로만 때린다고 생각하자

# 만든거 - 메소드 사용
def insertion_sort(arr):
  n = len(arr)
  for i in range(1, n):
    for j in range(i):
      if arr[i] < arr[j]:
        ins_value = arr[i+1]
        arr.insert(j+1, ins_value)
        del arr[i+1]
  return arr

# 모범답안 - 메소드 안사용
def insertion_sort(arr):
  n = len(arr)
  for i in range(1, n):
    new = arr[i]
    j = i - 1
    # i 부터 끝까지 내려오면서 비교
    while j >= 0 and arr[j] > new:
      arr[j+1], arr[j] = arr[j], arr[j+1]
      j -= 1
    arr[j+1] = new
  return arr
```
### 수행시간

**O(n^2)**
- for 루프는 n-1번 순환
- while 루프는 최대 i-1번 순환 : 내림차순으로 정렬되있을 경우 i가 늘어날 때 무조건 i-1번 수행
- 가장 좋은 경우 : 이미 오름차순으로 정렬된 경우에는 while이 돌지 않는다

**배열이 거의 정렬되어 입력되는 경우**
- 삽입 정렬은 배열이 이미 정렬된 상태라면 그냥 끝남 - O(n)
- 버블 정렬에서 표식자를 넣어서 두번째 for문이 돌아갔는지 판단했는데, 삽입정렬 같은 경우는 이미 정렬되어 있는 경우에는 **아예 while문이 안 돌기 때문에** 표식자 넣은 버블 정렬보다 더 효율적
- 버블 정렬에서의 표식자라는 여분의 코드 장치는 오버헤드를 일으킬 수 있다

**정리**
- 선택/버블 정렬 : n개짜리 배열에서 시작하여 아직 정렬되지 않은 배열의 크기를 하나씩 줄인다
- 삽입 정렬 : 1개짜리 배열에서 시작하여 이미 정렬된 배열의 크기를 하나씩 늘린다

## 힙정렬(Heap sort)
### 정의
힙을 이용해 정리를 하는 알고리즘

### 힙
이진트리, 맨 아래층을 제외하고는 완전히 채워져 있고 맨 아래층은 왼쪽부터 꽉 채워져 있음  
각 노드의 값은 자기 자식의 값보다 작음(min heap)
꽉 찬 이진트리이기 때문에 그냥 리스트로도 구현 가능  
A[k]의 자식은 A[2k]와 A[2k+1]  

###make heap
1. 맨 뒤에서부터 따져서 힙 성질에 관해 문제가 생길 수 있는 첫번째 원소를 대상으로 체크(뒤에서부터 따졌을 때 자식이 있는 최초의 노드부터 따지기 시작)
2. 따지는 노드의 값이 자식보다 클 경우, 따지는 노드를 자식 자리로 내림
3. 다음 순번 노드에 반복
4. 중간에 루트가 자식 중 작은 값보다 크지 않은 경우를 만나면 중단
```python
def make_heap(arr, n):
  for i in range(n//2, 0, -1):
  # n//2는 루트가 아닌 노드 중 맨 마지막 노드의 인덱스
    heapify(arr, i, n)

def heapify(arr, k, n):
  left, right = 2k, 2k+1
  # 양쪽 자식을 다 가지고 있는 경우
  if right <= n:
  # 좌우부터 비교해서 작은 값을 smaller로
    if arr[left] < arr[right]:
      smaller = left
    else:
      smaller = right
  # 왼쪽 자식만 가진 경우
  elif left <= n:
    # 왼쪽을 smaller로
    smaller = left
  # 리프노드인 경우
  else:
    return
  # 재귀적으로 따라가면서 리프까지 내리기, 아닌 경우 그냥 종료
  if arr[smaller] < arr[k]:
    arr[k], arr[smaller] = arr[smaller], arr[k]
    heapify(arr, smaller, n)
```
n/2번의 히피파이를 수행함 => 수행시간은 O(log n)이 아니라 O(n):이유 이해하기  

### heap sort
#### 동작
맨 끝 노드를 루트로 옮긴 후, 루트에 대한 히피파이를 수행하여 자리를 찾게 한다  
루트의 값을 맨 마지막 값으로 옮기니, min heap에서는 최소값이 계속 뒤로 이동하는 셈이고, 내림차순 정렬이 가능하다  

```python
def heap_sort(arr, n):
  make_heap(arr,n)
  # n-1번 도는 for문, i는 맨 끝 인덱스를 가리킴
  for last in range(n-1, 1, -1):
    arr[0], arr[last] = arr[last], arr[0]
    # 루트에서 내려간 노드 하나를 제외한후 루트에 대하여 히피파이(i-1)
    heapify(arr, 0, last)
```
#### 수행 시간
- makeheap : O(n)시간
- for루프는 n-1번 순환
- heapify는 O(log n)시간
- 대충 봤을 때는 O(n log n)

