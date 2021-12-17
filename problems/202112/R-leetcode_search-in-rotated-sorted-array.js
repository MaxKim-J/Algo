var search = function(nums, target) { //O(logn), O(1)
  // 문제분석
  
  // 오름차순으로 정렬되어있는 배열, 유니크함, 1보다 큰 인덱스 => length가 1일때
  // 꼭 연속된 모든 수가 다들어가있지는 않음. 다만 유니크
  // 인덱스를 기반으로 회전되어있음. 기반한 인덱스가 제일 앞으로 오는 형식
  // 여기에서 검색을 해내야댐 => target값을 찾고 현재 배열에서 인덱스 반환
  // logn 안으로 구해라 => 이거는 이진탐색인데 정렬하지 못하는...
  
  //! 평가하는 시점에서 정상적으로 추론될 수 있는 범위를 가지고 이분탐색하기(여기서는 정렬된 부분)
  
  let left = 0;
  let right = nums.length - 1;
  
  while(left <= right) {
      const mid = Math.floor((left + right) / 2)
      if (nums[mid] === target){
          return mid //* left보다는 mid를 잡아내는 이진탐색이 더 깔끔한듯(앞으로 걍 이렇게 하자)
      } else if (nums[left] <= nums[mid]) { // 중간값이 Left보다 큼(왼쪽이 정렬되어 값 예상 가능한 부분)
          if (target >= nums[left] && target < nums[mid]) { 
              // 왼쪽으로 범위 줄임
              right = mid - 1
          } else { 
              // 오른쪽으로 범위 줄임
              left = mid + 1
          }
      } else { // 중간값이 Left보다 작음(오른쪽이 정렬되어 값 예상 가능한 부분)
          if (nums[mid] < target && target <= nums[right]) {
              // 오른쪽으로 범위 줄임
              left = mid + 1
          } else {
              // 왼쪽으로 범위 줄임
              right = mid - 1
          }
      }
  }
  
  return -1
};