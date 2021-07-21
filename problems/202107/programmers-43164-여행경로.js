// 간단하게 생각하기
// 문제 똑바로 읽기 (ICN..)
// 거의 그냥 이건 재귀에 가까움
// 중복되는 비행기표를 가지고 있을때를 생각해야만 답이 제대로 나옴 - 사실 문제가 좀..더러움

function solution(tickets) {
  let answer = [];

  const DFS = (airport, tickets, path) => {
    let newPath = [...path, airport];
    if (tickets.length === 0) {
      answer.push(newPath);
    } else {
      tickets.forEach((ticket, idx) => {
        if (ticket[0] === airport) {
          // 출발지인걸 다 찾음
          let newTickets = [...tickets];
          const [[from, to]] = newTickets.splice(idx, 1);
          DFS(to, newTickets, newPath);
        }
      });
    }
  };

  DFS("ICN", tickets, []);
  return answer.sort()[0];
}
