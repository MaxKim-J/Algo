/*
숫자의 범위 확인하기(0보다 큰 정수)
코너케이스 => 인풋에 대한 인밸리데이션을 손코딩 과정에서는 보여주는게 좋을거 같음

[ 1,2,3,4 ] => -1
[ 1,1,2,3 ] => -1
[ 1,1,1,2,3 ] => 1
[ 1,1,1,2,2,2 ] => -1
[ 2,2,2,2,1,1 ] => 2 => 어떤 한 수가 배열에서 절반보다 큰 빈도로 나타난다면, 다른 수는 그렇게 안됨

엣지 케이스에 해당하는 케이스도 적어놓기
[1] => 1
[] => -1

힌트를 주면 코드로 옮겨보기
*/

const solution = (arr) => {
  if (arr.length === 0) {
    // 이런거 약간 쇼맨쉽으로 필요함ㅋㅋㅋ
    return -1;
  }

  if (arr.length === 1) {
    return arr[0];
  }

  const counter = {};
  const length = arr.length;
  for (let i = 0; i < length; i++) {
    if (counter[arr[i]] === undefined) {
      counter[arr[i]] = 1;
    } else {
      counter[arr[i]] += 1;
    }

    if (counter[arr[i]] > arr.length / 2) {
      return arr[i];
    }
  }
  return -1;
};

console.log(solution([1, 2, 3, 4]));
console.log(solution([1, 1, 2, 3]));
console.log(solution([1, 1, 1, 2, 3]));
console.log(solution([1, 1, 1, 2, 2, 2]));
console.log(solution([2, 2, 2, 2, 1, 1]));
console.log(solution([2]));
