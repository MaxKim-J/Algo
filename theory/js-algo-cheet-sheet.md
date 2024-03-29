# JS로 알고리즘 풀기 칱싵

## 1. Swap

구조분해 할당을 사용해 swap을 편하게 할 수 있다.

```js
const arr = [1, 2, 3, 4, 5];

[arr[1], arr[2]] = [arr[2], arr[1]];
```

### 변수에 넣으면 안된다.

```js
const arr = [1, 2, 3, 4, 5];
let a = arr[0];
let b = arr[1];
[a,b] = [b,a] // 이거는 안됨 배열에서 바로참조해야함
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
- `[...set]` => 집합 배열로 만들기

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
### Slice

slice는 문자열과 배열의 sub을 리턴하는데 사용한다. 

  - 새로운 subString, subArray를 반환한다.
  - 음수 인덱스를 사용할 수 있다.

### Splice

splice는 배열을 직접 수정할때 사용한다. 특정 인덱스에 삽입 삭제 모두 가능. 두번째 인자가 deletcount

- 음수 인덱스 얘도 사용 가능함
- 리턴값으로 없어진 값이 나온다.
- splice(0,5) : idx 0부터 5개 삭제
- splice(5,1) : idx 5 하나 삭제
- splice(0,0,'cat') : idx 0에 cat 추가 : 중간에 0이 오면 삽입이다, 어떤 것도 빼지 않음
- splice(0,1,'dog') : idx 0을 dog로 대체
- splice(0,0,'dog', 'cat') : idx 0에 dog, cat 추가

### 헷갈리는 포인트

- 배열의 마지막 값을 제거하고 싶을 경우 : `arr.splice(arr.length-1, 1);`
  - 제거는 그 인덱스부터 시작
  - 그냥 pop써도 되긴 하겠다..
- 배열의 마지막에 값을 넣고싶을 경우(push) : `arr.splice(arr.length, 0, 무언가);`
  - arr.length-1 기준으로 삽입하면 뒤에서 두번째에 삽입됨.
  - 여러번 push를 작성해야 하는 것을 막아주기도 하는건가..? 싶었는데 push도 인자 여러개 받을 수 있구나 ㄷㄷ
## 5.5 음수 인덱스

- 파이썬의 그것과는 매우 양상이 다르다. splice에서 사용하는 음수 인덱스는 `뒤에서부터 몇번째`의 의미이다. -1은 맨 뒤 인덱스에서부터 첫번째
- 맨 마지막 인덱스에 splice해서 삽입하고 싶다면, `splice(arr.length, 0, ...요소)` 이런식으로 해야함
- 왠만하면 음수 인덱스를 안 쓰는 것도 방법일수도 괜히 헷갈린다

## 6. Number의 정수 범위

![이런 문제가 나와서 정리해보았다..](https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/559/)

- Number의 정수 범위는 2**53-1(8바이트) 까지로 (9007199254740991, 음수도 그럼) 16자리부터는 못쓰는 숫자가 존재하고 17자리부터는 무조건 못쓴다고 보면 된다. 이때는 BigInt를 쓰거나 해야함
- BigInt로 연산할때는 숫자 뒤에 n을 붙인다.

## 7. 일정한 규칙으로 배열 만들기

- python에서는 리스트 컴프리헨션이나 `[0]*10` 이렇게 해도 리스트가 만들어지지만....
- 배열의 요소가 기본형일 경우 : `Array(n).fill(elem)`
  - 참조형을 fill하면 배열 내부의 요소들이 같은 레퍼런스를 가리키는 배열이나 객체가 되서 모든게 한번에 변함;;
- 배열의 요소가 배열이나 객체같은 참조형일 경우 : `Array.from({length:n}, (v,i) => {})`

## 8. Array.prototype.sort()

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

## 9. 쌩 for문 기점 쉽게 잡기

- 너무 기본기라 간과하기 쉽지만, 당황하면 은근히 안읽히는게 쌩 포문 코드다.
- 항상 for문 순회시 초기값은 무조건 순회에 포함된다
- 올라가는 포문 : 등호 없으면 끝값-1 까지 순회
```js
const arr = [1,2,3,4,5,6];

// < : 초기값부터 끝값 - 1 까지 순회
for (let i = 0;i<arr.length;i++) {
  console.log(i) // 0, 1, 2, 3, 4, 5
}

// <= : 초기값부터 끝값 까지 순회
for (let i = 0;i<=arr.length;i++) {
  console.log(i) // 0,1,2,3,4,5,6
}
```

- 내려가는 포문 : 등호 없으면 끝값+1 까지 순회
```js
const arr = [1,2,3,4,5,6];
// 초기값부터 끝값 + 1까지 순회
for (let i = arr.length;i>0;i--) {
  console.log(i) // 6, 5, 4, 3, 2, 1
}

// 초기값부터 끝값까지 순회
for (let i = arr.length;i>=0;i--) {
  console.log(i) // 6, 5, 4, 3, 2, 1, 0
}
```

## 10. 유니코드 변환

- 은근 코테에 유니코드 변환을 활용해야 하는 문제가 자주는 아니지만 드문드문 보인다.
- `str.charCodeAt(index)` : 특정 문자열 인덱스의 유니코드 변환
  - 인자를 아무것도 안넣으면 맨 앞캐릭터
- `String.fromCharCode()` : 유니코드 숫자를 문자로 변환
- 아스키 테이블 순서 : 시작하는 번호를 알고있으면 좋을 것 같다.
  - `48`~57 : 0부터 9까지(문자열)
  - `65`~90 : 알파벳 대문자
  - `97`~122 : 알파벳 소문자

## 11. 올림, 반올림, 버림

- Math.ceil : 올림
- Math.round : 반올림
- Math.floor : 버림, 파이썬의 //

## 12. 포문 선택 기준

JS에 for문이 많은데, 용도나 기능이 달라서 선택하기 애매할때가 많다. 코드를 작성하면서도 풀이가 달라질 수 있기 때문에 경험상 제일 좋은것은 쌩포문. 쌩포문은 포문에서 되야 하는 것이 다 된다.

크게 신경쓸건 아니지만 속도도 젤 빠르다.

- 인덱스에 바로 접근 가능(`for..of`, `for..in` 불가능)
- break, continue 사용 가능(`forEach`는 불가능)

```js
const arr = [1,2,3,4,5];
for(let i = 0;i<arr.length;i++) {
  console.log(arr[i]);
}


```

(그런 일이 많이는 없었던 것 같지만) 객체를 순회하고 싶을때는 인덱스는 별로 안중요하기 때문에 `for...in`을 주로 사용하는 듯 하다.

## 13. 난수

Math.random()으로 만든다. 기본적으로 0부터 1까지의 float난수를 반환하며, Math.floor로 정수로 변환한다.

- 정수 범위 난수 : 뒤에다가 정수를 곱한다. 제일 많이 씀.
  - `Math.floor(Math.random() * 4)` : 0부터 3까지의 정수
  - `Math.floor(Math.random() * 5)` : 0부터 4까지의 정수
  - `Math.floor(Math.random() * 5 + 1)` : 1부터 4까지의 정수
  - `Math.floor(Math.random() * 8 + 2)` : 2부터 7까지의 정수

