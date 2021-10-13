const fs = require("fs");
const filePath =
  process.platform === "linux" ? "/dev/stdin" : "./problems/202110/input.txt";
let input = fs.readFileSync(filePath).toString().split("\n");

/*
자바스크립트로 푼 첫번째 백준 문제!!!
플로이드 와샬을 구현한 뒤 i->j에서 j->i로 갈 수 있는지 확인만 하면 되는 문제였다
확실히 디버깅이 어렵다... 좀더 꼼꼼하게 실수를 하지 않아야 한다
*/

const [V, E] = input[0].split(" ").map((v) => +v);

const graph = Array.from({ length: V }, (v, i1) =>
  Array.from({ length: V }, (v, i2) => (i1 === i2 ? 0 : Infinity))
);

const dist = Array.from({ length: V }, (v, i1) =>
  Array.from({ length: V }, (v, i2) => (i1 === i2 ? 0 : Infinity))
);

for (let i = 0; i < E; i++) {
  const [a, b, c] = input[i + 1].split(" ").map((v) => +v);
  graph[a - 1][b - 1] = c;
  dist[a - 1][b - 1] = c;
}

for (let i = 0; i < V; i++) {
  for (let j = 0; j < V; j++) {
    for (let m = 0; m < V; m++) {
      if (dist[j][m] > dist[j][i] + dist[i][m]) {
        dist[j][m] = dist[j][i] + dist[i][m];
      }
    }
  }
}

let result = Infinity;

for (let i = 0; i < V; i++) {
  for (let j = 0; j < V; j++) {
    if (i !== j && graph[j][i] !== Infinity && dist[i][j] !== Infinity) {
      const cycleWeight = dist[i][j] + graph[j][i];
      result = Math.min(result, cycleWeight);
    }
  }
}

console.log(result === Infinity ? -1 : result);
