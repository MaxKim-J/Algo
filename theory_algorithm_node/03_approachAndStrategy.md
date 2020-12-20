# 03_approach and strategy

## how to improve

- devise a plan for solving problem
- master common problem solving pattern

## order

1. understand
2. explore concrete example
3. breakdown
4. solve/simplify
5. lookback/refactor

### 1 - understand

- 문제의 답이 바로 떠오르는 일같은건 일어나지 않는다
- 뭘 쓰기 전에 잘 읽어야된다 
- restate the problem in my own word
- input???? output??? and what of those look like : 인풋이 엄청 큰 메모리를 차지하거나 하는 경우도 생각해보기, 타입을 생각해보기
- output determined from the input? => enough infortation to solve problem : 조건을 구체화할 필요가 있음. 인터뷰라면 질문을 한다
- label the data : essential in problem => 인풋과 아웃풋, 그리고 필요한 변수들을 구체화하기

### 2 - explore example

- 테스트케이스들을 잘 분석해야함 => 더 많은 정보를 겟하기
- 심플한 케이스부터 검증 => 복잡한 테스트 케이스 => invalid한 인풋이면 => 빈 인풋이라면? => 경계조건?(edge cases)
- 이런식으로 조건을 만들어봐야 되는 과정

### 3 - break down

- 절차적으로 분해, 말로 써보기
- basic component of solution
- build skeleton : 뭐 주석으로 써놓는다던지

### 4 - solve/simplify

- 풀던가 아직 못풀겠으면 simple하게 만들어라
- 생각이 안나는건 넘어가고 주위 문제들을 먼저 해결해라
- simplify : 도저히 어떻게 못하겠는거(core difficulty) => 일단 무시, 단순한 솔루션을 쓰기 => 나중에 그걸 합쳐보기
- 더 main한 솔루션은 뭐지?
- 잘못된 선택을 안하는게 중요하니까, 점차점차 코드를 붙이는게 좋다. 잘못된 길로 들면 파멸함
- 시작하기 전에 fixating 하지말고 점차점차! => 뭔가는 확실히 해야겠다는 판단이 드는 것부터 실행에 옮긴다
- No Bias : 모든 답을 정해놓고 생각하면 안됨

### 5 - refactor/lookback

- 이게 진짜 효율적인가? 부터 생각
  - loop, 반복, 재귀
  - 정규식같은거를 아스키를 이용하는 charCode 같은걸로 바꾼다거나 `charCodeAt`
- 다른 방법은 없는지?
- 한번 보고 이해 쌉가능한가?
- 리팩터링 할 수 있는 다른 방법은?
  - if문 삼항연산자나 ||나 &&으로 만든다거나
  - 함수를 분리한다거나
- 다른 인간들은 어캐풀었?

## strategy

master common problem solving => common approaching

### Frequency Counter

- collect values/freqeuncies of values
- avoid nested loops or n^2 operation with array, string

```js
same([1,2,3], [4,1,9]) // true

// naive, O(n^2)
function same(arr1, arr2) {
  if(arr.length !== arr2.length) {
    return false
  }
  for (let i = 0;i < arr1.length;i++) {
    let correctIndex = arr2.indexOf(arr1[i] ** 2) // unnecessary roof
    if(correctIndex === -1) {
      return false
    }
    arr2.splice(correctIndex, 1)
    return true
  }
}

// refactor, O(n) - 이중포문보다 포문 여러개가 더 낫다
function same(arr1, arr2) {
  if(arr1.length !== arr2.length) {
    return false
  }
  let frequencyCounter1 = {}
  let frequencyCounter2 = {}
  for(let val of arr1) {
    frequencyCounter1[val] = (frequencyCounter1[val] || 0) + 1
  } 
  for(let val of arr2) {
    frequencyCounter1[val] = (frequencyCounter1[val] || 0) + 1
  } 
  // 데이터를 문제를 해결하기 쉬운 방향으로 수정한 예
  for(let key in frequencyCounter1) {
    if(!(key ** 2 in frequencyCounter2)) {
      return false
    }
    if(frequencyCounter2[key ** 2] !== frequencyCounter1[key]) {
      return false
    }
  } 
  return true
}
```

- anagram example
- To compare individual pieces, order, consistency,,,

```js
// 한쪽의 빈도를 평가
function validAnagram(first,second) {
  if(first.length !== second.length) {
    return false
  }
  const lookup = {}

  for (let i = 0;i<first.length;i++) {
    let letter = first[i]
    lookup[letter] ? lookup[letter] += 1 : lookup[letter] = 1
  }

  for (let i = 0;i<second.length;i++) {
    let letter = second[i]
    // 0일경우에도 방어됨
    if(!lookup[letter]) {
      return false
    } else {
      lookup[letter] -= 1
    }
  }
  return true
}

validAnagram('aaax', 'xaa')
```

### Multiple pointers pattern

```js
// naive
// 하나 잡아서 더해서 0되는거 찾다가 못찾으면 넘어가고
// 반복되는 순회, 반복되는 연산
function sumZero(arr) {
  for(let i = 0;i<arr.length<i++) {
    for(let j = 0;j<arr.length<j++) {
      if(arr[i] + arr[j] === 0) {
        return [arr[i], arr[j]]
      }
    }
  }
}

// refactor
// 한 배열에서 순회의 포인트를 두개를 잡는 방법으로 최적화
function sumZero(arr) {
  let left = 0;
  let right = arr.length - 1;
  while(left < right) {
    let sum = arr[left] + arr[right]
    if(sum === 0){
      return [arr[left], arr[right]]
    } else if (sum > 0) {
      right--;
    } else {
      left++;
    }
  }
}
```

- unique value

```js
// 내 풀이 O(n)
function countUniqueValues(arr) {
    if(arr.length < 2) {
        return arr.length
    }
    
    let count = 0;
    let firstPointer = 0;
    let secondPointer = 1;

    while(secondPointer <= arr.length) {
        if(arr[firstPointer] !== arr[secondPointer]) {
            count += 1
            firstPointer = secondPointer
        }
        secondPointer++
    }
    return count
}

// 아저씨 풀이
// 포인터가 두개라면 한 배열을 두개처럼 쓸수도 있다(;;)
// 하나는 순회, 다른 하나는 체크
// 극단적인 절약풀이...(count 변수도 필요없음) 그래도 한번은 돈다 O(n)
function countUniqueValues(arr) {
    // 어,...? 빈배열 넣으면 어캄 1나오는데
    var i = 0;
    for(var j = 1;j<arr.length;j++) {
      if(arr[i] !== arr[j]) {
        i++;
        arr[i] = arr[j]
      }
    }
    return i + 1;
}
```

### sliding window

- subset of data like string, array evaluate continuos
- useful for keeping track of a subset of data in an array/string etc

```js
// naive - O(n^2)
// 그냥 연속하는 개수를 다 더해서 그중에 큰거
function maxSubarraySum(arr, num) {
  if(num > arr.length) {
    return null
  }
  // 옹 이거머임
  let max = -Infinity
  for(let i = 0; i < arr.length - num + 1; i++) {
    temp = 0;
    // 근데 이거는 비용이 큰 순회는 아니긴함
    for (let j = 0;j < num;j++) {
      temp += arr[i+j]
    }
    if(temp > max) {
      max = temp
    }
  }
  return max
}

// refactor
// 순회로 할 연산을 인덱싱 값 연산으로 대체하는 경우
function maxSubarraySum(arr,num) {
  let maxSum = 0;
  let tempSum = 0;
  if(arr.length < num) return null
  // 앞에 연속된 Num개 만큼의 요소 총합
  for (let i = 0;i<num;i++) {
    maxSum += arr[i]
  }
  tempSum = maxSum
  for (let i = num;i < arr.length;i++) {
    // 자연스럽게 맨 처음값을 빼주고 다음값을 더해주는 메타
    tempSum = tempSum - arr[i - num] + arr[i]
    maxSum = Math.max(maxSum, tempSum)
  }
  return maxSum;
}
```

### divide and conquer

- dividing a dataset into smaller chunks and then repeating a process with a subset of data
- ex) binary search : O(n) => O(사실상 1)