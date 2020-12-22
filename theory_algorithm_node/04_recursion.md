# 04_recursion

process(a function in our case) calls itself
## 왜 쓰나

- 선형적인 반복을 입체적으로 바꾼다. 인자의 수를 줄이고 계속 반복되는 연산을 브레잌다운한다. 
- JSON.parse/stringify : 이것도 재귀적으로 작동한다, traversal
- iteration의 clear한 대안
- 이터레이션의 대안이라는 말은, 이터레이션처럼 자료구조를 배열로 만들어 놓을 수 있거나, 순회를 잘만 사용할 수 있을 때 굳이 재귀를 이용할 필요가 없다는 것이다. 단일한 자료구조로 정리하기 어렵거나, 연산이 단순 순회보다는 얼추 복잡해서 쉬운 자료구조로 회귀시키기 어려울때 사용한다? 라고 말해도 되려나

## 갑분 콜스택

- 재귀는 콜스택에 계속 같은 함수를 집어넣는다. 그리고 어디선가에서 끝남
- 끝나지 않는 재귀는 콜스택에서 계속 쌓이다가 exceeded

## helper method recursion

```js
function func1(arr) {
  let result = []
  function helper(helperInput) {
    if(helperInput.length === 0) {
      return
    }
    if(helperInput[0] % 2 !== 0) {
      result.push(helperInput[0])
    }
    helper(helperInput.slice(1))
  }
  helper(arr)
  return result
}
```

- 전역변수로 뭐 하나 놓고 다른 함수를 혼자 재귀하게 해서 전역변수에다가 뭔가를 기록하고 그 계산값을 리턴하던지 하는 패턴
- 프로그래머스 같은데서 활용할 수 있을듯

## pure recursion

```js
function func1(arr) {
  let newArr = []

  if(arr.length === 0) {
    return newArr
  }
  if(arr[0] % 2 !== 0) {
    newArr.push(arr[0])
  }

  result = result.concat(func1(arr.slice(1)))
  return result
}
```

- 부수효과가 없는 순수한 재귀함수. 재귀의 결과가 순수하게 리턴되고 합쳐짐 먼가 숏코딩 가능
- slice, spread operator, concat : 새로운 배열 리턴