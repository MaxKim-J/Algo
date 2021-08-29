function solution(table, l, p) {
  const jobs = [];
  const pTable = {};

  table.sort();

  table.forEach((row, i1) => {
    row.split(" ").forEach((elem, i2) => {
      if (i2 === 0) {
        jobs.push(elem);
        return;
      }

      if (pTable[elem] === undefined) {
        pTable[elem] = [0, 0, 0, 0, 0];
      }

      pTable[elem][i1] = 6 - i2;
    });
  });

  const result = Array.from({ length: 5 }, () => 0);

  l.forEach((lang, i1) => {
    pTable[lang].forEach((s, i2) => {
      result[i2] += p[i1] * s;
    });
  });

  const index = result.reduce(
    (acc, cur, idx) => (cur > result[acc] ? idx : acc),
    0
  );
  return jobs[index];
}
