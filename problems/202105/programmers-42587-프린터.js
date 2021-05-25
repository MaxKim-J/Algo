function solution(priorities, location) {
  let indexes = [...Array(priorities.length).keys()];
  const printed = [];

  while (printed.slice(-1)[0] !== location) {
    let fwd = priorities[0];
    let print = indexes[0];

    for (let i = 1; i < priorities.length; i++) {
      if (fwd < priorities[i]) {
        print = indexes[i];
        fwd = priorities[i];
      }
    }
    if (print === indexes[0]) {
      printed.push(print);
      priorities = priorities.slice(1);
      indexes = indexes.slice(1);
    } else {
      priorities = priorities.slice(1).concat([priorities[0]]);
      indexes = indexes.slice(1).concat([indexes[0]]);
    }
  }

  return printed.length;
}
