function solution(B, Y) {
  for (let i = 1; i <= Math.sqrt(Y); i++) {
    if (Y % i === 0 && B === (Y / i) * 2 + i * 2 + 4) {
      return [Y / i + 2, i + 2];
    }
  }
}
