// BFS, O(n), O(n)
var coinChange = function(coins, amount) {
  // amount값을 가장 적은 coin 가짓수로 만들기l
  // 그리디? => 값이 남아버리는 수가 있음
  // 동전 빼내기? 
  // coins의 정렬여부

  //! 관념에 의해 풀지 말고 문제를 검증해보기
  
  // 약간 BFS같은 느낌의 DP - 배열 하나 계속 돌려쓰기 + 중복없애기
  //! 재귀로도 비슷하게 할 수 있음
  //! 완탐 -> 하향식 -> 상향식
  const memo = new Set([amount])
  const queue = [[amount, 0]]
  
  while (queue.length) {
      const [elem, depth] = queue.shift();
      
      if (elem === 0) {
          return depth
      }
      
      for (let coin of coins) {
          const newElem = elem-coin;
          if (!memo.has(newElem) && newElem >= 0) {
              queue.push([newElem, depth+1])
              memo.add(newElem)
          }
      }
  }
  
  return -1;
};

// DP, O(amount * coins)
//! 왠만하면 상향식이 제일 우아한 풀이가 되더라(점화식 때문에)
function coinChange(coins, amount) {
  dp = new Array(amount + 1).fill(Infinity)
  dp[0] = 0

  for (let coin of coins) {
    // 해당 동전 값부터 끝까지
    for (let i=coin;i<amount+1;i++) {
      dp[i] = min(dp[i], dp[i-coin] + 1) // 기존 or 코인 하나 추가
    }
  }

  return dp[amount] !== Infinity ? dp[amount] : -1 // 변화 있으면 dp값 리턴
}
  