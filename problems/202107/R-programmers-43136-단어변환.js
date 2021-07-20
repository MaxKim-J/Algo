// 메모이제이션으로 BFS의 depth를 구하는 방법

function solution(b, t, words) {
  const len = b.length;

  let depth = 1;
  let queue = [b];
  let visited = {};

  let queueLength = 1;

  while (queue.length) {
    const cur = queue.shift();
    queueLength -= 1; // shift를 할 때마다 하나씩 까준다

    const available = words.filter((v) => {
      let diff = 0;
      for (let i = 0; i < len; i++) {
        if (cur[i] !== v[i]) {
          diff += 1;
        }
      }
      return diff === 1 && visited[v] === undefined;
    });

    for (let w of available) {
      if (w === t) {
        return depth;
      }
      queue.push(w);
      visited[w] = true;
    }

    // 맨 초기의 큐랭 변수를 다 소진했다면 한 depth가 끝났다는 이야기니까
    // 그때 depth를 추가해주고 length를 갱신해준다
    if (queueLength == 0) {
      depth += 1;
      queueLength = queue.length;
    }
  }

  return 0;
}
