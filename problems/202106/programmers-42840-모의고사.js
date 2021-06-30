function solution(a) {
  const crt = { 1: 0, 2: 0, 3: 0 };
  const methods = [
    [1, 2, 3, 4, 5],
    [2, 1, 2, 3, 2, 4, 2, 5],
    [3, 3, 1, 1, 2, 2, 4, 4, 5, 5],
  ];

  const len = a.length;
  for (let i = 0; i < len; i++) {
    methods.forEach((m, idx) => {
      if (m[i % m.length] === a[i]) {
        crt[idx + 1] += 1;
      }
    });
  }

  // console.log(crt)
  let answer = [];
  let max = 0;
  for (let j = 1; j < 4; j++) {
    if (crt[j] > max) {
      answer = [j];
      max = crt[j];
    } else if (crt[j] === max) {
      answer.push(j);
    }
  }

  return answer.sort((a, b) => a - b);
}
