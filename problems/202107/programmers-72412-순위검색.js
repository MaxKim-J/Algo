// 카카오 2021

// 내 코드 - 객체로 일종의 DB 자료구조를 만들고 쿼리를 분석해서 데이터셋에 접근하는 방법
// 탐색 트리를 사용해서 물론 일일히 찾아보는 것 보다는 검색 성능이 좋지만
// 결국 쿼리를 하나씩 분석해서 depth만큼 들어가야한다는게 시간의 낭비를 가져옴 => 정확성은 다 맞았지만 효율성은 다 틀림
// 찾아야 하는 데이터가 루트에 모여있게 만들어서 접근 시간을 줄이는게 현명한 접근이었음

function mySolution(I, Q) {
  const apply = {};

  for (let i = 0; i < I.length; i++) {
    let target = apply;
    I[i].split(" ").forEach((info, idx) => {
      if (idx !== 4) {
        if (target[info] === undefined) {
          target[info] = info === "chicken" || info === "pizza" ? [] : {};
        }
        target = target[info];
      } else {
        target.push(+info);
      }
    });
  }

  const result = [];

  for (let j = 0; j < Q.length; j++) {
    let queryArr = Q[j].split(" and ");
    queryArr = [...queryArr.slice(0, 3), ...queryArr[3].split(" ")];

    let target = [apply];
    queryArr.forEach((exp, idx) => {
      let newTarget = [];
      if (idx !== 4) {
        target.forEach((look) => {
          if (exp === "-") {
            for (const key in look) {
              if (Array.isArray(look[key])) {
                newTarget = newTarget.concat(...look[key]);
              } else {
                newTarget.push(look[key]);
              }
            }
          } else {
            if (look[exp] !== undefined) {
              if (Array.isArray(look[exp])) {
                newTarget = newTarget.concat(...look[exp]);
              } else {
                newTarget.push(look[exp]);
              }
            }
          }
        });
        target = newTarget;
      } else {
        result.push(
          target.reduce((acc, curr) => (curr >= exp ? acc + 1 : acc), 0)
        );
      }
    });
  }
  return result;
}

// 남의 코드 - info를 분석해서 나올 수 있는 쿼리를 재귀로 조합하여 구하고
// 트리에서의 빠른 접근을 구현하기 위해 객체의 키로 넣고 점수를 배열에다 저장함
// 결국 숫자만 구하면 된다는 점에서 굉장히 정답지향적인 접근
// 그리고 쿼리 객체에 모인 배열 중에서 쿼리의 마지막 숫자보다 더 큰 값을 찾기 위해
// 이진탐색을 이용해서 선형탐색에 소요되는 시간까지 줄임

function solution(info, query) {
  const answer = [];
  const infoMap = {};

  function combination(array, score, start) {
    const key = array.join("");
    const value = infoMap[key];

    if (value) {
      infoMap[key].push(score);
    } else {
      infoMap[key] = [score];
    }

    for (let i = start; i < array.length; i++) {
      const temp = [...array];
      temp[i] = "-"; // 전체를 모든 순서에 하나씩 더 넣어서 재귀를 돌림
      combination(temp, score, i + 1);
    }
  }

  for (const e of info) {
    const splited = e.split(" ");
    const score = Number(splited.pop());
    combination(splited, score, 0); // 조합으로 가능한 쿼리에 대한 모든 조합을 탐색해서 키로 삼아 값을 저장
  }

  for (const key in infoMap) {
    infoMap[key] = infoMap[key].sort((a, b) => a - b); // 이진탐색을 하기 위한 오름차순 정렬
  }

  for (const e of query) {
    const splited = e.replace(/ and /g, " ").split(" ");
    const score = Number(splited.pop());
    const key = splited.join("");
    const array = infoMap[key];

    if (array) {
      // start와 end는 index!!
      let start = 0;
      let end = array.length;

      // start에다가 값이 저장되는 이진탐색
      // score보다 이상인 첫번째 값의 인덱스를 찾음
      while (start < end) {
        const mid = Math.floor((start + end) / 2);

        // 해당 스코어가 어디 인덱스에 있는지를 찾음
        if (array[mid] >= score) {
          end = mid;
        } else if (array[mid] < score) {
          start = mid + 1;
        }
      }

      // 전체 길이에서 start를 빼면 그거보다 이상인 값의 개수가 나옴
      const result = array.length - start;
      answer.push(result);
    } else {
      answer.push(0);
    }
  }

  return answer;
}
