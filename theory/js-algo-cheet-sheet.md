# JS로 알고리즘 풀기 칱싵

## 1. Swap

구조분해 할당을 사용해 swap을 편하게 할 수 있다.

```js
const arr = [1, 2, 3, 4, 5];

[arr[1], arr[2]] = [arr[2], arr[1]];
```

## 2. 변수 여러개 동시에 선언

쉼표를 사용하면 선언자를 한번만 써도 된다

```js
const a = 5, b = 2, c = 3, d = {}, e = [];
```

이것도 구조분해할당의 한 유형인거 같은데, 이렇게도 된다

```js
const [a,b,c,d] = [0,1,2,3]
```

## 3. 집합 관련 연산

- add : 넣기
- delete : 빼기
- size : 크기
- new Set(배열) : 배열로 집합만들기
- [...set] => 집합 배열로 만들기

## 4. 이진 연산

- & : and
- | : or
- ~ : not
- << : 왼쪽이동
- >> : 오른쪽 이동
- ^ : XOR
- >>>, <<< : 두칸씩 이동
- toString(2) : 이진법 문자열로 변환
- parseInt(숫자, 2) : 이진법을 정수로 변환

## 5. splice, slice

- slice는 문자열과 배열의 sub을 리턴하는데 사용한다. 
  - 새로운 subString, subArray를 반환한다.
  - 음수 인덱스를 사용할 수 있다.
- splice는 배열을 직접 수정할때 사용한다. 특정 인덱스에 삽입 삭제 모두 가능. 두번째 인자가 deletcount
  - 음수 인덱스 얘도 사용 가능함
  - 리턴값으로 없어진 값이 나온다.
  - splice(0,5) : idx 0부터 5개 삭제
  - splice(5,1) : idx 5 하나 삭제
  - splice(0,0,'cat') : idx 0에 cat 추가
  - splice(0,1,'dog') : idx 0을 dog로 대체
  - splice(0,0,'dog', 'cat') : idx 0에 dog, cat 추가


## 6. Number의 정수 범위

![이런 문제가 나와서 정리해보았다..](https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/559/)

- Number의 정수 범위는 2**53-1 까지로 (9007199254740991, 음수도 그럼) 16자리부터는 못쓰는 숫자가 존재하고 17자리부터는 무조건 못쓴다고 보면 된다. 이때는 BigInt를 쓰거나 해야함
- BigInt로 연산할때는 숫자 뒤에 n을 붙인다.

## 7. 일정한 규칙으로 배열 만들기

- python에서는 리스트 컴프리헨션이나 `[0]*10` 이렇게 해도 리스트가 만들어지지만....
- 배열의 요소가 기본형일 경우 : `Array(n).fill(elem)`
  - 참조형을 fill하면 배열 내부의 요소들이 같은 레퍼런스를 가리키는 배열이나 객체가 되서 좋지 못함
- 배열의 요소가 배열이나 객체같은 참조형일 경우 : `Array.from({length:n}, (v,i) => {})`

## 8. Array.sort()

- JS의 정렬 메소드는 해괴하게 생겼다.
- 콜백이 없으면 요소들은 문자열로 취급되어 유니코드 값 순서대로 정렬된다.
- 새로운 배열을 반환하지 않고 기존의 배열을 직접 수정한다.
- 규칙 : compare(a,b)가 리턴하는 값이 0보다 작은 경우 a를 b보다 낮은 색인으로 정렬, 0을 반환하면 서로에 대해 변경하지 않고 모든 다른 요소에 대해 정렬, 0보다 큰 경우 b를 a보다 낮은 인덱스로 정렬.

```js
const arr = [3,4,5,2];

function compare(a, b) {
  if (이 조건에 따르면 a가 b보다 작다.) {
    return -1;
  }
  if (이 조건에 따르면 a가 b보다 크다.) {
    return 1;
  }
  // a가 b와 동일한 경우!
  return 0;
}

sort((a,b) => a-b) // 숫자 배열 오름차순 정렬
sort((b,a) => b-a) // 숫자 배열 내림차순 정렬
sort((a,b) => a.value - b.value) // 특정 프로퍼티로 정렬

// value 속성에 대해 내림차순, value2 속성에 대해 오름차순 정렬
sort((a,b) => {
	if(a.value>b.value) return 1; // 내림차순 정렬
	if(a.value<b.value) return -1;
	if(a.value2<b.value2) return 1; // 오름차순 정렬
	if(a.value2<b.value2) return -1;
	return 0;
}) 

// 이게 읽기에 더 나은듯 - value 속성에 대해 오름차순, value2 속성에 대해 내림차순
sort((a,b) => a.value !== b.value ? a.value - b.value : b.value2 - a.value2) 
sort((a,b) => a[0] !== b[0] ? a[0] - b[0] : b[1] - a[1]) 
```