// table에서의 퍼즐칸(1), game_board에서의 빈칸(0) 추출
// 그 두칸의 번호를 모두 뽑아서 한가지 방향과 0,0으로 시작하는 모양으로 만듬(약간의 정규화)
// 대조, 비교해서 같으면 조각이 맞는거
// 진짜.. 모든 과정을 다 구현하려고 하지 말자 진짜..지름길을 찾자!
// 비교하기 좋게 만들어 비교하기

function dfs(table, x, y, list, find) {
  // 우, 좌, 하, 상
  const dx = [1, -1, 0, 0];
  const dy = [0, 0, 1, -1];
  const stack = [[x, y]];
  const len = table.length;
  list.push([x, y]);

  while (stack.length) {
    let [a, b] = stack.pop();
    let moveX, moveY;
    table[y][x] = -1;

    // 우, 좌, 하, 상 순으로 stack에 저장
    for (let i = 0; i < 4; i++) {
      moveX = a + dx[i];
      moveY = b + dy[i];

      // 이동한 좌표가 테이블에서 벗어나 있는 경우는 제외
      if (moveX < 0 || moveX >= len) continue;
      if (moveY < 0 || moveY >= len) continue;

      // 이동한 좌표의 값이 찾고자 하는 값과 일치하면 stack과 list에 push하고, 다녀갔다는 표시 (-1 처리)
      if (table[moveY][moveX] === find) {
        table[moveY][moveX] = -1;
        stack.push([moveX, moveY]);
        list.push([moveX, moveY]);
      }
    }
  }
}

function rearrange(list) {
  const minX = Math.min(...list.map((c) => c[0])); // 가장 왼쪽에 있는 값의 x
  const minY = Math.min(...list.map((c) => c[1])); // 가장 왼쪽의 있는 값의 y
  return list.map((c) => [c[0] - minX, c[1] - minY]).sort(); // 이게 참 충격적이군..
}

function rotate(list) {
  if (list.length === 1) return list;
  let result = [];
  let shape = list.map((l) => l);
  let width =
    Math.max(...shape.map((s) => s[1])) - Math.min(...shape.map((s) => s[1]));
  let height =
    Math.max(...shape.map((s) => s[0])) - Math.min(...shape.map((s) => s[0]));
  let w;

  for (let i = 0; i < 4; i++) {
    let temp = rearrange(shape.map((c) => [c[1], width - c[0]]));
    shape = temp;
    result.push(shape);
    w = width;
    width = height;
    height = w;
  }

  return result.sort()[0];
}

function solution(game_board, table) {
  let answer = 0;
  // spaces: 게임판의 빈 칸 리스트, puzzles: 테이블의 퍼즐 리스트
  let spaces = [],
    puzzles = [];

  for (let y = 0; y < table.length; y++) {
    for (let x = 0; x < table[0].length; x++) {
      // game_board의 칸이 빈 칸(0)일 경우
      if (game_board[y][x] === 0) {
        let space = [];
        dfs(game_board, x, y, space, 0); // 해당 칸과 이어지는 칸 탐색
        space = rearrange(space); // (0,0)에서 시작하는 모양으로 재정렬
        space = rotate(space); // 어떤 방향이더라도 한 방향의 모양으로 변형
        spaces.push(space);
      }
      // table의 칸이 블록(1)일 경우
      if (table[y][x] === 1) {
        let puzzle = [];
        dfs(table, x, y, puzzle, 1); // 해당 칸과 이어지는 칸 탐색
        puzzle = rearrange(puzzle); // (0,0)에서 시작하는 모양으로 재정렬
        puzzle = rotate(puzzle); // 어떤 방향이더라도 한 방향의 모양으로 변형
        puzzles.push(puzzle);
      }
    }
  }

  for (let space of spaces) {
    for (let i = 0; i < puzzles.length; i++) {
      if (JSON.stringify(space) === JSON.stringify(puzzles[i])) {
        answer += puzzles[i].length;
        puzzles = puzzles.map((p, idx) => (idx === i ? [] : p));
        break;
      }
    }
  }

  return answer;
}
