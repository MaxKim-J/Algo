var findMin = function(nums) {
  // 인풋 
  // 회전 - 오른쪽으로 돌리기
  // 오름차순 정렬되어있는 배열을 회전시킴
  // 배열의 요소는 모두 유니크
  // 회전된 배열을 입력으로 받아 배열의 최소값을 리턴
  // 배열은 하나 이상의 요소 => 하나 요소 등의 엣지케이스

  /*
    입출력 분석

    1. 인풋, 회전은 오른쪽으로 돌리는 것 뜻함
    2. 오름차순 정렬된 배열을 회전시킴
    3. 배열 요소 모두 유니크
    4. 회전된 배열을 입력으로 받아 배열의 최소값을 리턴
    ! 5. 배열은 하나 이상의 요소 => 배열 요소 하나일때 엣지케이스
  */

  /*
    O(n)보다 빠르게 구해야함 
    첫번째 요소부터 탐색을 시작하면 값이 증가하다가 갑자기 뚝 떨어지는 시점이 있거나
    없을 것이다(첫번째가 가장 작은 경우)
  */
  
  const length = nums.length;

  // 첫값이 끝값보다 작은 경우 맨 앞 요소가 가장 작다
  // 혹은 요소가 하나일경우 요소가 하나일경우는 nums[0] === nums[0]
  if (nums[0] <= nums[length - 1]) {
      return nums[0]
  }
  
  // 그렇지 않은 경우, 양쪽 끝을 이용해서 탐색을 하면 될 것 같은데
  // 양쪽 끝에서부터 출발하여 
  
  // 둘중에서 먼저 찾으면 리턴
  for (let i = 0;i<length;i++) {
      // 첫값에서 시작한 탐색은 값이 작아지기 시작하는 지점을 찾는다
      if (nums[i] > nums[i+1]) {
          return nums[i+1]
      }
      
      // 끝값에서 시작한 탐색은 값이 커지기 시작하는 지점을 찾는다
      if (nums[length-i-1] < nums[length-i-2]) {
          return nums[length-i-1]
      }
  }
}; // O(n)보다 빠르고, 공간복잡도는 O(1)


// 이진탐색, O(logn), O(1)
// 전환 시작점을 대충 mid로 잡고 이진탐색으로 푸는 방법도 있음
/*
def findMin(self, nums):
  left, right = 0, len(nums) - 1

  # 값 자체를 조건으로 활용. 오른쪽이 왼쪽보다 커지는 경우라면, left가 곧 찾고자 하는 포인트
  while nums[left] > nums[right]:  # 왼쪽 값이 오른쪽보다 큰 경우 
      middle  = (left + right) // 2  # 중간 어딘가를 찾음
      if nums[middle] < nums[right]: # middle의 값이 오른쪽보다 적으면
          right = middle # 범위를 왼쪽으로 줄이고(middle위는 다 정렬되어있어서 볼필요가 없음)
      else:
          left = middle + 1 # 아니면 범위를 오른쪽으로 줄임(middle아래는 다 정렬되어있어서 볼필요가 없음)
  return nums[left]
*/

