function solution(price, money, count) {
  const result =
    money -
    Array.from({ length: count }, (v, i) => i).reduce((acc, curr) => {
      return acc + (curr + 1) * price;
    }, 0);

  return result > 0 ? 0 : -result;
}
