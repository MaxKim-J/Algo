const containsDuplicate = function(nums) {
    
  // 입출력 : 정수/자연수 배열, 빈배열, 2개 이상의 중복
  
  // 중복된 수가 존재하면 true
  // 모두 유니크하다면 false
  
  // 빈도배열 시간:O(N), 공간:O(N)
  const count = {}
  for (let elem of nums) {
      if (count[elem] === undefined) {
          count[elem] = true
      } else {
          return true
      }
  }
  return false    

  // 정렬해서 붙어있는 경우 : O(nlogn), O(1)
  
};