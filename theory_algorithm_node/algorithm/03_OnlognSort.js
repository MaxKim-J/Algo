// O(nlogn) 정렬 알고리즘 - 병합정렬, 퀵정렬, 그리고 특정 상황에서 더 빠른 계수정렬
const sample1 = [8,67,4,5,23,12]
const sample2 = [8,67,4,5,23,12]
const sample3 = [8,67,4,5,23,12]

// 1 - merge sort

function merge(arr1, arr2) {
  let result = [];
  // arr들의 포인터 각자
  let i = 0;
  let j = 0;
  // 배열 어느 한쪽이 다 순회를 마칠때까지
  while(i < arr1.length && j < arr2.length) {
    if(arr2[j] > arr1[i]) {
      result.push(arr1[i]);
      i++;
    } else {
      result.push(arr2[j]);
      j++;
    }
  }
  // 순회를 마쳤다면, 아직 순회가 덜 끝난 배열의 요소들을 다 배열로 집어넣는다
  while(i < arr1.length) {
    result.push(arr1[i]);
    i++;
  }
  while(j < arr2.length) {
    result.push(arr2[j]);
    j++;
  }
  return result;
}
function mergeSort(arr) {
  // 재귀적으로 더이상 나눠지지 않을때까지 이등분
  if(arr.length <= 1) return arr;
  let middlePoint = Math.floor(arr.length/2);
  let left = mergeSort(arr.slice(0,middlePoint));
  let right = mergeSort(arr.slice(middlePoint));
  console.log(left,right)

  // 재귀적으로 더이상 나눠지지 않을 때까지 이등분하면 하나씩만 남는데
  // 그걸 가지고 merge를 시작해서 다시 합침

  // 먼저 다 나눈다음에, 아직 콜스택이 안 끝나고 기다리는 상황에서 merge까지 하면 콜스택이 날라감
  // 그 merge한 값을 받아서 다시 다음 콜스택에서는 left right 처리한후 merge 처리해서 콜스택 다시 날림
  return merge(left,right);
}

console.log(mergeSort(sample1))

// 시간복잡도 - 모든 경우에 O(nlogn): 자료를 순회하면서 부수고 합치고 정렬하는데 n, 그걸 logn번 반복함
// 꼭 2개가 아니라 3개로 나누고 합친다고 하더라도, 층의 수는 logan인데, log2로 고칠 수 있기 때문에 그저 nlogn
// 공간복잡도 - O(n), 병합할때 새로운 배열들을 계속 만들어주기 때문에 그렇다

// 2 - quick sort
// 이상적으로 뽑아야할 pivot 값은 배열의 중간값이다
// 공간복잡도 최적화된 버전(재귀로 새로운 배열 만들거나 그러지 않음)

function pivot(arr, start=0, end=arr.length-1) {
  let pivot = arr[start];
  let swapIndex = start;
  // 맨 앞의 원소를 기본 피봇으로 하고, 그 뒤부터 순회
  for(let i = start + 1;i < arr.length; i++) {
    // 피봇이 순회한 elem보다 크다면 둘이 스왑
    // 스왑 인덱스는 피봇보다 작은 값이 위치한 배열 일부의 끝 인덱스를 가리키게 된다
    if(pivot > arr[i]) {
      swapIndex++;
      [arr[i], arr[swapIndex]] = [arr[swapIndex], arr[i]]
    }
  }
  [arr[start], arr[swapIndex]] = [arr[swapIndex], arr[start]]
}

function quickSort(arr, left = 0, right = arr.length - 1) {
  // 하나만 남았을때 == 정렬이 다 끝났음
  if(left < right) {
    let pivotIndex = pivot(arr, left, right)
    // 왼쪽
    quickSort(arr, left, pivotIndex-1)
    // 오른쪽
    quickSort(arr, pivotIndex+1, right)
  }
  return arr;
}

// 3 - radix sort