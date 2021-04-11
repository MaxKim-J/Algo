# JSPS Cheat Sheat

JS로 PS같은거 하지마라...

## 순열과 조합

조합 : 몇개중 몇개 뽑는데 순서는 상관없음(순서 상관없이 똑같은게 들어가만 있으면 같은 케이스, 숫자가 정해져있다면 걍 n개의 for문으로도 가능, 혹은 DFS라던지)  
순열 : 몇개중 몇개 뽑는데 순서 상관있음(다른 케이스로 침)

```js
function combination(arr, selectNum) {
  const result = [];
  if (selectNum === 1) return arr.map((v) => [v]);
  arr.forEach((v, idx, arr) => {
    // 수 하나를 박아놓고 그 나머지것들로 나눠서 생각 => 이전 idx와 이후 idx 사이에 있는 값은 못 뽑음
    const fixed = v;
    const restArr = arr.slice(idx + 1);

    // 하나는 이미 선택된 셈이므로 하나 빼서 재귀
    const combinationArr = combination(restArr, selectNum - 1);
    const combineFix = combinationArr.map((v) => [fixed, ...v]);
    result.push(...combineFix);
  });
  return result;
}

function permutation(arr, selectNum) {
  let result = [];
  if (selectNum === 1) return arr.map((v) => [v]);

  arr.forEach((v, idx, arr) => {
    // 수 하나 박아놓는 것은 똑같으나 값이 아니라 인덱스로 같고 다른것 처리
    // 이전 idx와 이후 idx사이의 값도 뽑을 수 있음
    const fixer = v;
    // 당장 뽑은 수와 인덱스가 다른 것들을 다 들고감 그냥
    const restArr = arr.filter((_, index) => index !== idx);

    const permuationArr = permutation(restArr, selectNum - 1);
    const combineFixer = permuationArr.map((v) => [fixer, ...v]);
    result.push(...combineFixer);
  });
  return result;
}
```

## 이차원배열 깊은복사

알고리즘 푸는데 lodash나... JSON을 사용할수는 없으니 대충 수동으로 해줘야된다  
선형배열은 걍 전개연산 쓰면 된다...지만 안에 객체가 있다면 어떨까..?(근데 PS에서..? 그런일이 흔하지는 않을듯)

```js
// 뭐 약간 이정도?
function deepCopy(arr) {
  const new_arr = [];
  for (const sub_arr of arr) {
    new_arr.push([...sub_arr]);
  }
  return new_arr;
}
```

## range대신에 쓸수있는 것들

```js
const a = [...Array(5).keys()]; // 0, 1, 2, 3, 4

const b = Array.from(new Array(5), (x, i) => i); // 0, 1, 2, 3, 4
```

## 에라토스테네스의 체

JS에서는 Range가 없으니 그냥 keys로 레인지 배열 만들기..

```js
function eratos(num) {
  const arr = [...Array(num).keys()];
  for (let i = 2; i < Math.sqrt(num); i++) {
    for (let j = i + i; j < num; j += i) {
      arr[j] = -1;
    }
  }
  return arr.filter((elem, idx) => elem !== -1 && idx > 1);
}
```

## 정렬, 다중조건 정렬

### 정렬

Array.sort()

```js
const a = [9, 2, 5, 2, 4, 1, 3];

a.sort((a, b) => {
  console.log(a, b);
});

// 각 비교마다
// 2 9
// 5 2
// 2 5
// 4 2
// 1 4
// 3 1
```

- compare callback이 제공되지 않으면 요소를 문자열로 변환하고 유니코드 순서로 문자열을 비교하여 정렬됨. 즉 숫자 정렬은 제대로 안됨
- callback의 리턴값에 따라서 정렬의 양상이 바뀜
  - 리턴값이 0보다 작은 경우 a를 b보다 낮은 색인으로 정렬 => a가 b보다 먼저옴(원래)
  - 리턴값이 0인 경우 정렬하지 않음
  - 리턴값이 0보다 큰 경우 b를 a보다 낮은 색인으로 정렬 => b가 a보다 먼저옴(뒤집음)
- compare 함수는 순수함수여야함
- 모두 숫자일 경우, return a - b 라고 하면 무조건 오름차순으로 정렬함. return b - a는 내림차순. 뭔가 원리에 따른것이 아니라 걍 편의를 위해서 이렇게 만들어둔것 같음??
- 조건문으로 -1, 0, 1을 리턴하는 식으로 조건에 따른 정렬을 할 수도 있음

### 다중조건 정렬

참 눈에 안들어오는 sort 내부의 콜백을 바꿔주면 된다

```python
 sorted_arr = sorted(dic.items(), key = lambda x:(x[1], x[0]))
```

```javascript
// 극혐인걸..?

const obj = {
  1: 2,
  2: 3,
  4: 2,
};

const sorted_arr = Object.entries(obj).sort((a, b) => {
  // [1]로 오름차순 정렬
  if (a[1] > b[1]) return 1;
  if (a[1] < b[1]) return -1;
  // [1]이 같다면 [0]으로 오름차순 정렬
  if (a[0] > b[0]) return 1;
  if (a[0] < b[0]) return -1;
});
```
