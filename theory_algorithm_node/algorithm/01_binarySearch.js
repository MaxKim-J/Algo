// ex1)
// arr은 정렬된 것을 조건으로 한다
function binarySearch(arr, elem) {
  let start = 0;
  let end = arr.length - 1;
  let middle = Math.floor((start + end) / 2)  

  while(start <= end) {
    if (elem < arr[middle]) {
      end = middle - 1
    } else {
      start = middle + 1
    }
    middle = Math.floor((start + end) / 2)
  }
  return arr[middle] === elem ? middle : -1;
}

console.log(binarySearch([2,5,6,9,13,15,28,30], 15))
console.log(binarySearch([2,5,6,9,13,15,28,30], 50)) // 8 7 7 stucked => 경계조건 예외처리, 없을때

/*
worst,average = O(log n) : 탐색할 배열이 계속 절반으로 줄어들기 때문에 O(n) 보다 작음
근데 정렬된 배열을 기준으로 하기때문에 정렬해서 돌릴경우 최악은 O(nlogn) 이상이 될 수 있음 
best = O(1) : 한번만 순회한다면 상수연산만 하다가 끝남(한번에 찾아진다면)
*/