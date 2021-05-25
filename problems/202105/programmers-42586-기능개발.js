function solution(progresses, speeds) {
  const answer = [];
  while (progresses.length) {
    for (let i = 0; i < progresses.length; i++) {
      progresses[i] += speeds[i];
    }

    let deploy = 0;

    for (let j = 0; j < progresses.length; j++) {
      if (progresses[j] < 100) {
        break;
      } else {
        deploy += 1;
      }
    }

    if (deploy > 0) {
      progresses.splice(0, deploy);
      speeds.splice(0, deploy);
      answer.push(deploy);
    }
  }
  return answer;
}
