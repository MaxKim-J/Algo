// 약간 거리 최소값중 최대값이라고 하니까 좀 헷갈리는 게 있었다..
// 다시 말하면, 모든 돌들에 대해서 가능한 많이 거리를 띄워놓을 때의 최소값
// 그 공유기 문제랑 비슷함 => 문제가 참 해석이 어려움

function solution(distance, rocks, n) {
  let answer = 0;
  rocks = [0, ...rocks.sort((a, b) => a - b), distance]; // 이분탐색을 위해 정렬 오름차순

  // 거리의 값을 계속 이분탐색 해 나갈때
  // 남아있는 돌을 구함
  const BinarySearch = () => {
    let start = 0;
    let end = rocks[rocks.length - 1]; // 돌 중 최대값

    while (start <= end) {
      let mid = Math.floor((start + end) / 2);
      let count = 0,
        now = 0;

      // 자연스럽게 간격을 최대로 하면서 꺼낼 수 있는 돌을 구할 수 있음
      for (let i = 1; i < rocks.length; i++) {
        if (rocks[i] - now < mid) {
          // 거리가 설정한 최소값보다 작다면 얘는 삭제가 가능한 돌임 => 간격을 더 벌림
          count++;
        } else {
          now = rocks[i]; // 거리가 설정한 최소값 보다 큰 경우 다음 돌로 넘어감
        }
      }

      // 삭제하려는 돌보다 더 많은 돌을 삭제할 수 있을 경우
      if (count > n) {
        end = mid - 1;
      } else {
        start = mid + 1;
      }
    }

    answer = end;
  };

  BinarySearch();
  return answer;
}
