const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().split("\n");

const dr = [0, 0, 1, -1];
const dc = [1, -1, 0, 0];

const BFS = (sr, sc, w, h, board) => {
  const paths = [];
  const visited = Array.from({ length: h }, () =>
    Array.from({ length: w }, () => Infinity)
  );
  const queue = [[sr, sc, []]];

  while (queue.length) {
    const [r, c, doors] = queue.shift();
    for (let i = 0; i < 4; i++) {
      const nr = r + dr[i];
      const nc = c + dc[i];
      const newDoors = [...doors];
      // 갈 수 있는 상황에서 격자 밖으로 나가려면?
      if (nr < 0 || nr >= h || nc < 0 || nc >= w) {
        // 문을 열고 나갈수도 있다
        paths.push(doors);
      } else {
        if (visited[nr][nc] > doors.length) {
          if (board[nr][nc] !== "*") {
            if (board[nr][nc] === "#") {
              newDoors.push(`${nr}${nc}`);
            }
            queue.push([nr, nc, [...newDoors]]);
            visited[nr][nc] = doors.length;
          }
        }
      }
    }
  }
  return paths;
};

let p = 1;

for (let i = 0; i < +input[0]; i++) {
  const [h, w] = input[p].split(" ").map((v) => +v);
  const board = [];
  const prisoner = [];

  for (let j = 1; j < h + 1; j++) {
    const row = [];
    for (let m = 0; m < w; m++) {
      if (input[p + j][m] === "$") {
        prisoner.push([j - 1, m]);
      }
      row.push(input[p + j][m]);
    }
    board.push(row);
  }

  const paths1 = BFS(prisoner[0][0], prisoner[0][1], w, h, board);
  const paths2 = BFS(prisoner[1][0], prisoner[1][1], w, h, board);

  let result = Infinity;
  for (let p1i = 0; p1i < paths1.length; p1i++) {
    for (let p2i = 0; p2i < paths2.length; p2i++) {
      const pathSet = [...new Set(paths1[p1i].concat(paths2[p2i]))];
      result = Math.min(result, pathSet.length);
    }
  }

  console.log(result);

  p = p + h + 1;
}
