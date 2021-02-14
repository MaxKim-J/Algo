# 알고리즘 : 정렬 3
2020.02.04  
특수 정렬 알고리즘 - 기수정렬, 계수정렬  

최악의 경우에 정렬 시간이 O(nlogn)보다 빠른 알고리즘  
원소 두개를 비교함으로써 정렬하는 경우에는 최악의 경우 수행시간이 O(nlogn)보다 빨라질 수 없음  
그런데 입력 원소들이 특수한 성질을 만족하는 경우에는 O(nlogn)보다 빠른 정렬 알고리즘들이 존재함.  

## 계수정렬
### 동작
정렬하고자 하는 원소들의 값이 O(n)을 넘지 않는 경우에 사용 가능  
배열의 원소들이 k를 넘지 않는 자연수일 경우(k는 여기서 어떤 정수)   
1. 배열의 원소를 훑어보고 1부터 k의 자연수가 각각 몇번 나타내는지를 센다  
2. 이 정보를 토대로 A[0..n]의 각 원소가 몇번째에 놓이면 되는지를 계산한다  
### 구현
```python
def counting_sort(arr, K):
    # k값을 받아두고 빈배열 만든다
    # K를 기준으로 k보다 적은 값들에 해당하는 인덱스
    c = [0] * K
   
    # 정렬된 출력값이 들어갈 배열
    sorted_arr = [0] * len(arr)

    # 배열을 순회해서 값을 발견하면, c배열에서 그 값에 해당하는 인덱스를 올린다
    for i in arr:
        c[i] += 1

    # 배열 c에 기록된 값을 이전 요소들의 누적합으로 다시 할당한다
    for i in range(1,K):
        c[i] += c[i-1]
   
    # c를 기준으로 새로운 배열에 재배치
    for i in range(len(arr)):
        sorted_arr[c[arr[i]]-1] = arr[i]
​        c[arr[i]] -= 1 # 굳이 안해도 결과에는 영향 안미침

    return sorted_arr
```
### 시간복잡도
3개의 for 루프가 최대 O(n)까지 돌아가므로 O(n)  
일반적으로 계수 정렬은 k가 O(n)을 초과하지 않는 경우에 선형시간에 정렬하기 위해 사용  

## 기수정렬

### 동작
기수정렬은 입력이 모두 **k자릿수 이하**의 자연수인 특수한 경우에 사용할 수 있는 방법, O(n)
1. 가장 낮은 자리수만 가지고 모든 수를 정렬함
2. 가장 낮은 자릿수는 잊어버고 다음 자릿수를 가지고 다시 정렬
3. 더이상 자릿수가 남지 않을때까지 반복

0부터 9까지 표시된 10개 공간을 준비해놓고 각각의 수를 가진 입력은  
해당 공간에 차례대로 넣어준다는지 하는 방법을 사용할 수 있음  = (k*O(n))

### 구현
계수정렬을 활용하면 쉽다  
계수정렬을 활용하는 이유 : O(n)유지 + 10을 넘지 않을 것을 알고 있으므로 + 안정성도 유지  
*이렇게 하는 이유는?) 입력 데이터 A의 최대값인 k가 커지면 계수정렬의 효율성이 크게 떨어진다(인덱스와 값이 대응하기 때문에 배열이 무지하게 큰게 필요) 하지만 각각의 자릿수를 기준으로 정렬하게되면 계산복잡성을 낮출 수 있음  
```python
# 현재 자릿수(d)와 진법(base)에 맞는 숫자 변환
# 함수를 쓴다!
# ex) 102, d = 1, base = 10, : 2
def get_digit(number, d, base):
  return (number // base ** d) % base

# 자릿수 기준으로 counting sort
# A : input array
# position : 현재 자릿수, ex) 102, d = 1 : 2
# base : 10진수라면 base = 10
def counting_sort_with_digit(A, d, base):
    # k : ex) 10진수의 최대값 = 9
    k = base - 1
    B = [-1] * len(A)
    C = [0] * (k + 1)
    # 현재 자릿수를 기준으로 빈도수 세기
    for a in A:
        C[get_digit(a, d, base)] += 1
    # C 업데이트
    for i in range(k):
        C[i + 1] += C[i]
    # 현재 자릿수를 기준으로 정렬
    for j in reversed(range(len(A))):
        B[C[get_digit(A[j], d, base)] - 1] = A[j]
        C[get_digit(A[j], d, base)] -= 1
    return B

from math import log
def radix_sort(list, base=10):
    # 입력된 리스트 가운데 최대값의 자릿수 확인
    digit = int(log(max(list), base) + 1)
    # 자릿수 별로 counting sort
    for d in range(digit):
        list = counting_sort_with_digit(list, d, base)
    return list
```

### 안정정렬(Stable Sort)
값이 같은 원소끼리는 정렬 후에 원래의 순서가 바뀌지 않는 성질  
처음에 정렬되지 않은 상태에서의 같은 값들의 순서가 정렬 되고 난 후에도 유지되는게 안정 정렬   
불안정 정렬은 비교하는 과정에서 같은 원소끼리의 순서가 바뀔 가능성이 있음  

안정정렬 : 버블 정렬, 삽입 정렬, 병합 정렬, 기수 정렬
불안정 정렬 : 선택 정렬, 퀵 정렬
