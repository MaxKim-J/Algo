function solution(N) {
  // 집합을 좀더 자주 이용해보자
  const answer = new Set();
  const numbers = N.split("");

  const isPrime = (n) => {
    if (n < 2) return false;

    // 제곱근은 sqrt, 절대값이 abs...
    for (let i = 2; i <= Math.sqrt(n); i++) {
      if (n % i === 0) {
        return false;
      }
    }
    return true;
  };

  const recursion = (value, numbers) => {
    if (numbers.length === 0) return;

    const len = numbers.length;

    for (let i = 0; i < len; i++) {
      const num = value + numbers[i];
      if (isPrime(parseInt(num))) {
        answer.add(parseInt(num));
      }
      // 깊복 신경쓰자
      const temp = [...numbers];
      temp.splice(i, 1);
      recursion(num, temp);
    }
  };

  recursion("", numbers);

  return answer.size;
}
