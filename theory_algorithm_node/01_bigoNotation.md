# 01 BigO notation

- 코드의 성능을 일반화하고 이야기하는 방법  
- 구현하는 방법은 천차만별이지만, 성능을 일반화하여 이야기하면 평가가 가능  
- code labeling
- compare to others, useful for discussing trade-offs between different approaches
- 최적화에 필요함 + 코딩 인터뷰

## Timing Out Code

- faster, less memory-intensive, more readable
- 측정: performance 객체, time not reliable but tendency or measurement
- general trends

```js
let t1 = performance.now()
// execute
addUpTo(100000000000)
let t2 = performance.now()
console.log(`Time Elapsed ${(t2-t1)/1000} seconds`)
```

## counting operation

- count operation that **matters**, ignore tiny operations

```js
function addUpTo(n) {
    let total = 0;  // 할당
    for(let i = 0;i<=n;i++) { //할당, 더하기, 순회, 비교
        total += i  // 더하기
    }
    return total
}
```

## big o

- worse case scenario. count all operations that matter

```js
// O(n)
function addUpTo(n) {
    let total = 0;  // 할당
    for(let i = 0;i<=n;i++) { //할당, 더하기, 순회, 비교
        total += i  // 더하기
    }
    return total
}

//O(1)
function addUpTo2(n) {
    return n * (n+1) / 2
}
```

## simplify

- constant don`t matter (O(2n) => O(n), O(500) => O(1)) : 가장 큰 값에 비해 무시할만한 값이라서
- 인자는 데이터의 원래 크기
- 숫자연산, 할당은 상수시간
- 배열이나 객체에 접근하는 시간도 상수시간
- 반복문은 어떻게 순회되느냐에 따라 다름

## 공간복잡도

- 원시타입은 상수공간, 값이랑 상관없음
- 문자열은 O(n)
- 참조형은 프로퍼티 개수만큼 O(n)

## log

- 로그 시간 복잡도일때 밑은 별로 중요하지 않다 => 지수의 승수가 더 중요
- 8 => 4 => 2 => 1 : log8 = 3 - 이런식으로 상수시간보다 약간 위에있는 그래프, 값이 비례해서 연산이 n배씩 증가하거나 할때