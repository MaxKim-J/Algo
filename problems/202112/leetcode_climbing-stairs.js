var climbStairs = function(n) {
  // 계단을 오르는 방법은 총 몇개가 있는가?
  
  // DP - 일종의 피보나치수열
  
  // n은 45이하의 정수, 무조건 하나 이상 들어있음
  // n이 1이거나 2일때의 엣지케이스 고려
  const dp = [0, 1, 2]
  
  if (n < 3) {
      return dp[n]
  }
  
  
  for (let i = 3;i<n+1;i++) {
      dp[i] = dp[i-2] + dp[i-1]
  }
  
  return dp[n]
  
};