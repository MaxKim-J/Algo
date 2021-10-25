const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().split("\n");

// 변수명 블럭마다 유니크하게 해야 할거 같다
// BFS할때 격자 나가는 조건 제대로 표기하기(이거때문에 시간 ㅈㄴ걸림..)

const dr = [0, 0, 1, -1];
const dc = [1, -1, 0, 0];

const board = [];
const visited = [];

const [N, M] = input[0].split(" ");
for (let i = 1; i < input.length; i++) {
  const row = input[i].split("").map((v) => +v);
  board.push(row);
  visited.push(row.map((v) => (v === 1 ? -1 : 0)));
}

const regionMap = {};

const result = Array.from({ length: N }, () =>
  Array.from({ length: M }, () => 0)
);

let regionIdx = 1;

for (let i = 0; i < N; i++) {
  for (let j = 0; j < M; j++) {
    if (board[i][j] == 0 && visited[i][j] == 0) {
      const queue = [[i, j]];
      let count = 1;
      visited[i][j] = regionIdx;

      while (queue.length) {
        const [r, c] = queue.shift();
        const idx = [];
        for (let p = 0; p < 4; p++) {
          const nr = r + dr[p];
          const nc = c + dc[p];
          if (-1 < nr && nr < N && -1 < nc && nc < M) {
            if (visited[nr][nc] == 0 && board[nr][nc] == 0) {
              queue.push([nr, nc]);
              count += 1;
              visited[nr][nc] = regionIdx;
            }
          }
        }
      }

      regionMap[regionIdx] = count;
      regionIdx += 1;
    }
  }
}

for (let i = 0; i < N; i++) {
  for (let j = 0; j < M; j++) {
    if (board[i][j] == 1) {
      const idx = [];
      let count = 1;
      for (let p = 0; p < 4; p++) {
        const nr = i + dr[p];
        const nc = j + dc[p];
        if (-1 < nr && nr < N && -1 < nc && nc < M && board[nr][nc] == 0) {
          if (visited[nr][nc] !== -1 && !idx.includes(visited[nr][nc])) {
            count += regionMap[visited[nr][nc]];
            idx.push(visited[nr][nc]);
          }
        }
      }
      result[i][j] = count % 10;
    }
  }
}

console.log(result.map((v) => v.join("")).join("\n"));
