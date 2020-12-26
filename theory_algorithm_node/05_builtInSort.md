# 05_자바스크립트 빌트인 소팅

## sort()

- 문자열은 알파벳으로 정렬(스트링 유니코드)
- 콜백이 제공되지 않으면 요소를 문자열로 변환하고 유니 코드 포인트 순서로 문자열을 비교하여 정렬. 모든 elem들이 문자열로 바뀌어서 유니코드별로 정렬되게됨
- 그래서 걍 sort() 하면 숫자에는 적용이 안됨
- 그래서 comparator 콜백이 필요함
- O(nlogn)

## comaprator 콜백

- 이 콜백함수는 a,b 값의 쌍을 보고 함수의 리턴값에 따라 정렬을 수행하게 된다.
- 리턴값에 따라 어떻게 정렬을 할지 결정됨
- 음수를 리턴하면 a b : a를 b보다 낮은 색인으로 정렬
- 양수를 리턴하면 b a : b를 a보다 낮은 색인으로 정렬
- 0을 리턴하면 a와 b는 같음 : a와 b를 서로에 대해 변경하지 않고 모든 다른 요소에 대해 정렬
- 요 콜백은 순수함수로써, 요소 a와 b의 특정 쌍이 두개의 인수로 주어질 때 항상 동일한 값을 반환해야 함. 일치하지 않는 결과가 반환되면 정렬 순서는 정의되지 않음.

## 예시

### 오름차순 정렬

```js
function numberCompare(num1, num2) {
  return num1 - num2;
}

[6,4,15,10].sort(numberCompare);
// 4, 6, 10, 15
```

### 내림차순 정렬

```js
function numberCompare(num1, num2) {
  return num2 - num1;
}

[6,4,15,10].sort(numberCompare);
// 15, 10, 6, 4
```

### 문자열 길이순 정렬

```js
function compareByLen(str1, str2) {
  return str1.length - str2.length;
}

['aaa', 'aaaa', 'aaaaa', 'aaaaaa'].sort(compareByLen);
```
