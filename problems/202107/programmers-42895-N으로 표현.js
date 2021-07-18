// 테이블 각이 안나오면 캐싱 메모로 풀어야 할듯

// 너무 테이블에 맞춰 넣으려고 생각하면 답 안나옴. 결국 완전탐색에서 이동해야함(완전탐색과 DP의 연결고리..)
// 부분문제가 뭔지 생각해보자
// 사용한 숫자에 대한 값을 가지고 dp[6] = dp[1] ^ dp[5] + dp[2] ^ dp[4] + dp[3] ^ dp[3]... 이런식으로 앞에왔을때랑 뒤에왔을때 경우를 모두 구해줌
// 집합에 메모이제이션하는거 좋은듯(중복을 다 저장할 필요가 없음)

function solution(N, number) {
  // 캐싱은 집합의 배열, 인덱스가 곧 사용한 숫자의 개수가 됨
  const cache = new Array(9).fill(0).map((el) => new Set());
  for (let i = 1; i < 9; i++) {
    cache[i].add("1".repeat(i) * N); // 연속수 더해주기(맨처음에 5만 넣어줌)
    // 맨 처음 i=1 j=1이므로 0번재 칸부터 시작하고, 1번째칸(실제로는 2)
    for (let j = 1; j < i; j++) {
      for (const arg1 of cache[j]) {
        // 대신 캐싱
        for (const arg2 of cache[i - j]) {
          // 여기는 뭐 거의 완전탐색이랑 비슷하긴 함. 어쨌든 다 해봐야 알음
          cache[i].add(arg1 + arg2);
          cache[i].add(arg1 - arg2);
          cache[i].add(arg1 * arg2);
          cache[i].add((arg1 / arg2) >> 0);
        }
      }
    }
    // 캐싱을 하면서 찾아야 하는 값이 있는지 체크함
    if (cache[i].has(number)) return i;
  }
  return -1;
}
