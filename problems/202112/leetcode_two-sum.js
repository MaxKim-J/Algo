const twoSum = function(nums, target) {
    
  // nums 배열에는 정수, 0 들어갈 수 있음?
  // 인덱스 2개만 리턴됨
  // 모든 숫자는 Unique
  // 한 입력에 단 하나 솔루션
  // 출력 순서는 상관 없음
  
  // 두 합의 경우의수를 모두 구해야 할까?
  // O(n)으로 하는게 관건
  
  // 수를 하나 뺀 다음에 뺀 수가 있는지 보면 두번 순회만에 풀 수 있는거 아닌가
  const len = nums.length;
  
  // 뺀 수는 다른 배열공간같은거 이용
  const temp = {}
  for (let i = 0;i<len;i++) {
      temp[nums[i]] = i
  }

  // 순회하면서 target에서 뺀 값이 있는지 확인
  for (let j = 0;j<len;j++) {
      const tempIdx = temp[target-nums[j]];        
      if (tempIdx !== undefined && j !== tempIdx) {
          return [tempIdx, j]       
      }
  }
  
};

// 좀더 깔끔한 방법
//! 만약에 발견되지 않으면 어떻게 해야하나?
const twoSum2 = function(nums, target) {
  var map = {};

  for(var i = 0; i<nums.length; i++) {
      var num = nums[i];
      if(map[num] == undefined) {
        map[target-num] = i; // 연속된 메모리 구조에 뺀값을 키로, 인덱스를 값으로 넣기
      } else { // 나중에 해당값이 이미 map에 들어있다면 합으로 만들 수 있다는 뜻
        return [map[num], i];
      }
  }
};

