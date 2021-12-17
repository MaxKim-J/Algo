var maxSubArray = function(nums) {
    
  // 연속된 값들로 서브어레이 만듬
  // 서브어레이에 있는거는 하나 이상의 요소
  // 배열에는 정수, 0, 음수도 모두 들어감
  //! 요소는 하나 이상의 배열 - 1개, 2개일때의 엣지케이스 고려하기
  // 아웃풋은 합
  // 개수는 따로 정해지지 않앗죠
  
  // 순서를 보장해야하므로 정렬은 안되고
  // O(n)으로 해결할 수 있어야 함
  
  // 가져갈 것이냐 버릴 것이냐? 
  // 트리탐색, 재귀처럼 풀면 너무 오래걸리려나 => 반복되는 연산이 너무 많을듯
  
  // DP처럼, 해당 수를 순회했을때 가능한 값들을 배열에 저장해서 앞으로 가면 O(n)이 나온다
  
  // 엣지케이스 처리?
  
  let curr = nums[0];
  let answer = nums[0];
  
  for (let i=1;i<nums.length;i++) {
      curr = Math.max(curr + nums[i], nums[i])
      answer = Math.max(answer,curr)
  }
  
  return answer
  
};