// 집합 2개 사용 - O(n^2), O(n)
var threeSum = function(nums) {
  // 배열은 정수배열, 0 음수 자연수 모두 온다 - 중복되는 수가 없다
  const result = new Set()
  
  // 배열에는 빈배열이 포함될 수도 있다 => 빈배열일 경우 예외처리
  // 배여르이 수가 3개 미만인 경우에는 답이 없다 => 예외 처리
  if (nums.length < 3) {
      return []
  }
  
  // 3개를 합해서 0이 될수 있는 쌍의 숫자를 넣은 이차원 배열 리턴
  // 없는 경우 빈배열을 리턴
  
  // 하나를 먼저 뽑은 이후에 나머지 남은 배열의 숫자에서 2개를 뽑아서
  // 그 2개의 합이 기존의 합과 더해졌을 때 0이 되면 된다 => O(n^2)
  //! 답의 정렬 여부?? => 입출력 보는 상황에서 확인했어야함
  for (let i =0;i<nums.length;i++) {
      const target = 0 - nums[i]
      const countSet = new Set()
      // 여기서 빈도객체, 혹은 집합을 하나 만든다
      for (let j = 0;j<nums.length;j++) {
          if (i===j) continue
          // 나머지 배열에서 기존 뽑은 수를 0으로 만드는 쌍을 찾는다
          // 여러개가 될 수 있으니 모두 순회해야 한다
          // 중복이 되는 경우를 제한다 => 어캐하지 이거
          //! 이게 풀이 단계에서 헷갈릴 경우에는 짜피 뭐.. 이미 많이 진행된 경우이므로 그냥 직진하는게 나을 것 같다
          //! 나중에 말나오면 최적화하거나 하면 됨. 일단 빨리 푸는게 나을듯.
          //! 딱히 정답이 아닌것도 아니고 시간복잡도에 큰 영향 끼치는 것도 아님
          if (countSet.has(target-nums[j])) {
              const value = [nums[i], nums[j], target-nums[j]].sort((a,b) =>a-b).join(' ')
              result.add(value)
          } else {
              // 없는 경우 삽입
              countSet.add(nums[j])
          }
      }
  }
  
  // 집합 관련한 문법들 정리하기
  return [...result].map(v => v.split(' '))
};