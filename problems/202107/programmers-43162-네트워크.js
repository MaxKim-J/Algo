function solution(n, pc) {
  let answer = 0;
  const visited = Array(n).fill(false);

  for (let i = 0; i < n; i++) {
    if (visited[i] === false) {
      let queue = [i];
      visited[i] = true;

      while (queue.length) {
        //!!!!!!!!!!! 절대 배열로만 참거짓 판단을 해서는 안된다!!!!! 까먹지마셈...
        const value = queue.shift();
        pc[value].forEach((v, j) => {
          if (visited[j] === false && v === 1) {
            visited[j] = true;
            queue.push(j);
          }
        });
      }
      answer += 1;
    }
  }
  return answer;
}
