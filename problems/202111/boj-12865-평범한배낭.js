const fs = require("fs");
const filePath =
  process.platform === "linux" ? "/dev/stdin" : "../../input.txt";
let input = fs.readFileSync(filePath).toString().split("\n");

const [m, ...s] = input;
const [N, K] = m.split(' ').map((v) => +v);

const stuffs = [[0,0]].concat(s.map((v) => v.split(' ').map(v => +v)));
const dp = Array.from({length:N+1}, () =>
  Array.from({length:K+1}, () => 0)
);

for (let i = 1;i<N+1;i++) {
  for (let j = 1;j<K+1;j++) {
    const w = stuffs[i][0];
    const v = stuffs[i][1];
    dp[i][j] = j < w ? dp[i-1][j] : Math.max(v + dp[i-1][j-w], dp[i-1][j]);
  }
}

console.log(dp[N][K]);