// O(n^2) 정렬 알고리즘 - 버블정렬, 선택정렬, 삽입정렬

const sample1 = [8,67,4,5,23,12]
const sample2 = [8,67,4,5,23,12]
const sample3 = [8,67,4,5,23,12]

// 1 - Bubble Sort

// 최적화 1: 정렬된 배열이 들어왔을 경우에는 인자들을 평가해서 스왑할지말지 결정할 필요가 없음. 한번만 순회하면 됨 - O(n)
// 그걸 가능하게 해주기 위해서 변수가 하나 더 필요함
function bubbleSort(arr) {
  let noSwaps;
  for(let i = arr.length;i>0;i--) {
    // 비교해야하는 횟수는 i 루프를 돌 때마다 하나씩 줄어든다.
    // 매 루프마다 맨 마지막 elem은 정렬이 끝나기 때문에

    // es6문법 사용해서 이런 스왑 함수를 내부에 만들어줄 수도 있다
    const swap = (arr,idx1,idx2) => {
      [arr[idx1], arr[idx2]] = [arr[idx2], arr[idx2]];
    }
    noSwaps = true
    // 맨 끝에서 하나 앞부분까지만 가면 된다
    for(let j = 0;j <i - 1;j++) {
      if(arr[j] > arr[j+1]) {
        const temp = arr[j]
        arr[j] = arr[j+1]
        arr[j+1] = temp
        noSwaps = false
      }
    }
    if(noSwaps) break;
  }
  return arr
}

// 시간 복잡도 : 일반적으로 O(n^2) - 순회하면서 비교 O(n), 그 비교를 O(n)번
// 정렬된 배열이 어디에선가 만들어져서 중간에 리턴한다면 O(mn)

console.log('bubbleSort result ' + bubbleSort(sample1))

// 2 - Selection Sort : 뽑아 넣는다
function selectionSort(arr) {
  for (let i = 0; i<arr.length; i++){
    // 초기화
     let lowest = i;
     // 매번 이미 작은값 찾아 정렬된 그 이후의 배열만 보면 된다
     for(let j = i+1; j < arr.length; j++) {
       if(arr[j] < arr[lowest]) {
         lowest = j
       } 
     }
     // 가장 작은 값을 현재 평가되는 배열의 맨 앞에 놓으면 됨
     // 이때 lowest값이 이미 i인 경우에 대해서는 스왑을 진행하지 않음
     if(i !== lowest) {
      const temp = arr[i];
      arr[i] = arr[lowest];
      arr[lowest] = temp;
     }
  }
  return arr
}

console.log('selectionSort result ' + selectionSort(sample2))

// 시간복잡도 : 모든 경우에 O(n^2), 어쨋든 모든 횟수에 가장 작은값을 골라내긴 해야되서 루프 두개가 항상 살아있게 된다
// 모든 수가 정렬되어있는 경우에 swap이 0번 일어나긴 함

// 3 - Insertion Sort : 지자리를 찾아가게 만든다

// 두번째 elem부터 시작하고, 제자리를 찾기 위해 비교해야할 값은 요소 기준으로 앞에 위치한 요소

function insertionSort(arr) {
  for(let i = 1;i<arr.length;i++) {
    const currentVal = arr[i];
    for(let j = i - 1;j >= 0 && arr[j] > currentVal;j--) {
      [arr[j], arr[j+1]] = [arr[j+1],  arr[j]]
    }
  }
  return arr
}

console.log('insertionSort result ' + insertionSort(sample3))

// 시간복잡도 - 일반적으로 O(n^2), 다만 정렬된 배열이 인자로 들어왔을 경우, 
// 이미 평가할 요소들이 제자리에 있다고 판단하기 때문에 for문이 하나도 안돌아서 O(n)

// 공간 복잡도는 모든 경우에 O(1)로 구현 가능
