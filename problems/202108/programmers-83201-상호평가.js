function mySolution(s) {
  const getGrade = (score) => {
    if (score >= 90) {
      return "A";
    } else if (score >= 80 && score < 90) {
      return "B";
    } else if (score >= 70 && score < 80) {
      return "C";
    } else if (score >= 50 && score < 70) {
      return "D";
    } else if (score < 50) {
      return "F";
    }
  };

  let answer = "";
  const studentLen = s[0].length;

  for (let i = 0; i < s.length; i++) {
    let processedScore = [];
    let minValue = 100;
    let maxValue = 0;
    let minCount = 0;
    let maxCount = 0;

    for (let j = 0; j < studentLen; j++) {
      processedScore.push(s[j][i]);
      if (s[j][i] >= maxValue) {
        if (s[j][i] === maxValue) {
          maxCount += 1;
        } else {
          maxCount = 1;
          maxValue = s[j][i];
        }
      }
      if (s[j][i] <= minValue) {
        if (s[j][i] === minValue) {
          minCount += 1;
        } else {
          minCount = 1;
          minValue = s[j][i];
        }
      }
    }

    const isSelfOnlyMin = minCount === 1 && s[i][i] === minValue;
    const isSelfOnlyMax = maxCount === 1 && s[i][i] === maxValue;

    if (isSelfOnlyMin || isSelfOnlyMax) {
      processedScore = processedScore.filter((s, index) => index !== i);
    }

    const avg =
      processedScore.reduce((acc, cur) => acc + cur, 0) / processedScore.length;
    answer += getGrade(avg);
  }
  return answer;
}

// 솔루션중 가장 짧았던것
let solution = (scores) =>
  scores[0]
    .map((_, c) => scores.map((r) => r[c]))
    .map((s, i) => [...s.splice(i, 1), s]) // 어떤게 없는 모든 경우
    .map(
      ([m, s]) => (Math.min(...s) <= m && m <= Math.max(...s) ? [m, ...s] : s) // 이거 된다..
    )
    .map(
      (s) =>
        "FDDCBAA"[ // 10점 점수별로 인덱싱해서 컷팅하는 스킬, 객체에서 바로 참조하는 것처럼 인덱스만 구하면 레인지를 바로 알 수 있게끔 하네
          // 알아두면 좋은듯 map은 정말 여러 방식으로 구현이 가능한듯
          Math.max(parseInt(s.reduce((a, c) => a + c) / s.length / 10) - 4, 0)
        ]
    )
    .join("");
