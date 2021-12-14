//! 누가 봐도 풀이가 간결하게 떨어지려면 어떻게해야할까(넘 더럽다)
//! 이제 그걸 좀 고민해볼 단계인거같음

const maxProfit = function(prices) {
  /*
  기술면접에서 가능한 질문들
  
  1. 자연수 배열? 0이나 음수 가능?
  2. 빈배열 올수도 있음?
  */
  
  // 최대 이익을 리턴
  // 이전 것은 관심없음
  // O(n^2)이하로 풀기
  
  // 정렬하면 안됨 순서가 중요
  // 떨어지긴만 한다면 수익을 낼 수 없으므로 0 => 초기값
  
  // 최소값을 계속 이동시키는 방법
  let minIdx = 0;
  let maxIdx = 1;
  let profit = 0;
  
  while(maxIdx < prices.length) {
      if (prices[maxIdx] - prices[minIdx] < 1) {
          minIdx = maxIdx;
      } else {
          profit = Math.max(profit, prices[maxIdx] - prices[minIdx])
      }
      maxIdx++
  }
  
  return profit

};


// 가장 깔끔한 풀이
var maxProfit = function(prices) {
  // 값의 최저와 최고를 변수로 놓는다
  let max = 0;
  let min = prices[0]; // 현재까지 발견된 최소값
  
  // 순회
  for(let i = 0; i < prices.length; i++){
      let currPrice = prices[i]; // 현재 프라이스
      min = Math.min(min, currPrice); // 현재까지의 최소값 경신
      max = Math.max(max, currPrice-min) // 현재 가격에서 뺀 값을 갱신
  }
  
  return max;
};