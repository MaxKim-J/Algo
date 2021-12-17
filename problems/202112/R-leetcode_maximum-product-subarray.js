var maxProduct = function(nums) {
    
  // 연속된 부분배열 중 곱셈의 합이 가장 큰 구간의 값을 리턴
  // 배열은 정수배열, 0이나 음수 가능 => 0의 영향 고려
  // 배열의 요소는 non-empty, 1개 이상 => 1개, 2개 엣지케이스 고려
  
  // DP인데 곱셈으로? => 절대값이 문제가된다
  // 순회는 한번 하되, 모든 경우의 수를 고려한다 매번 round마다 배열을 살려놓는 방식으로 
  // 배열은 공간복잡도를 그나마 줄이기 위해 하나를 돌려서 사용한다
  
  // 역시 해는 명징하게
  
  let minFar = nums[0]
  let maxFar = nums[0]
  let answer = nums[0]
  
  // 지금까지 곱해왔던 것들 중 절대값이 가장큰 양수값과 음수값을 계속 저장해놓고 있다가
  // 현재 값과 곱해서 가장큰값, 가장 작은값을 계속 갱신시킨다
  // 답은 절대값이 가장 큰 양수값이랑만 비교하면 된다
  for (let i = 1;i<nums.length;i++) {        
      const tempMax = Math.max(nums[i], maxFar*nums[i], minFar*nums[i])
      minFar = Math.min(nums[i], maxFar*nums[i], minFar*nums[i])
      maxFar = tempMax
      answer = Math.max(maxFar, answer)
  }
  
  return answer
};

//! 역시 명징하지 않으면 해가 아니다