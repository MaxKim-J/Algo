const fs = require("fs");
const filePath =
  process.platform === "linux" ? "/dev/stdin" : "./problems/202110/input.txt";
let input = fs.readFileSync(filePath).toString().split("\n");

/*
어떤 지점에서 백트랙킹이 되어야 하는지 좀 더 잘 파악할 필요가 있었다 뻘짓을 넘 많이했음

결국 8번 넘게 벽이 아래로 내려왔는데도 무조건 queue에 무언가가 남아있다면 얘는 끝가지 갈 수 있음
visited를 적용하기 좀 어려운 상황이라서(요리조리 피하기 가능) set으로 불필요한 좌표가 queue에 들어가는 것을 막고
결국 set에 있는 것을 확인하는 방법으로 풀게 되었다
*/

const dr = [0, 0, 0, 1, -1, 1, -1, 1, -1];
const dc = [0, 1, -1, 0, 0, 1, -1, -1, 1];

let board = input.map((v) => v.split(""));

const moveBoard = () => {
  return [Array.from({ length: 8 }, (v) => ".")].concat(board.slice(0, 7));
};

const BFS = () => {
  let queue = new Set(["70"]);

  for (let i = 0; i < 8; i++) {
    const newQueue = new Set();
    for (let elem of queue) {
      const rc = elem;

      const r = +rc[0];
      const c = +rc[1];

      if (board[r][c] === "#") {
        continue;
      }

      for (let i = 0; i < 9; i++) {
        const nr = dr[i] + r;
        const nc = dc[i] + c;

        if (-1 < nr && nr < 8 && -1 < nc && nc < 8) {
          if (board[nr][nc] === ".") {
            newQueue.add(`${nr}${nc}`);
          }
        }
      }
    }
    queue = newQueue;
    board = moveBoard();
  }
  return [...queue].length === 0 ? 0 : 1;
};

console.log(BFS());
