// 정답지향적으로 이진탐색 풀기.
// 무슨 값을 찾아야 하는지만 제대로 설정할 수 있으면 절반은 풀린다
// 여기서 찾아야 하는 값은 검사할때 걸리는 시간의 최대값

const { time } = require("console");

function solution(n, times) {
  times.sort((a, b) => a - b);
  let left = 1; // 모든 검사가 마치는데 걸리는 시간의 최소값
  let right = n * times[times.length - 1]; // 걸릴수 있는 시간의 최대값 == 가장 큰수 * 사람수
  let answer = right;

  while (left <= right) {
    let mid = Math.floor((left + right) / 2);
    let count = 0;

    times.forEach((value) => {
      count += Math.floor(mid / value); // 검사까지 모두 걸리는 시간을 한 사람이 할 수 있는 시간으로 나눔 => 검사관 한명이 가능한 몫
      //! 가능한 모든 검사를 full로 했을때의 값임

      // 각 검사관 한명이 가능한 몫들의 합이 n을 최초로 넘어가면 => 최소의 시간이 나옴
      if (count >= n) {
        answer = Math.min(mid, answer); // 최솟값
        return;
      }
    });

    // 검사 가능한 사람의 값이 n보다 크면 오른쪽을 줄이고, 작으면 왼쪽을 줄인다
    if (count >= n) {
      right = mid - 1;
    } else {
      left = mid + 1;
    }
  }
  return answer;
}

const solution = (n, times) => {
  times.sort((a, b) => a - b);

  // 가장 작은 케이스와 가장 큰 케이스가 무엇인지 생각하기
  let left = 0;
  let right = times[times.length - 1] * n;
  let mid = Math.floor((left + right) / 2);

  while (left <= right) {
    //! mid 값 하나마다 검사관 모두가 full로 검사를 돌렸을 때 검사할 수 있는 닝겐수 == count
    // 어쨋든 mid시간 안에 처리할 수 있는 사람수와 전체 사람수를 놓고 구하기(여기서 스케쥴은 별 상관 없음)
    // 단순화해서 생각해야 했음

    const count = times.reduce(
      (result, cur) => result + Math.floor(mid / cur),
      0
    );
    if (count >= n) {
      right = mid - 1;
    } else {
      left = mid + 1;
    }
    mid = Math.floor((left + right) / 2);
  }

  return left;
};
