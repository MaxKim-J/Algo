/*
특정 기간의 가격 변화가 주어졌을 때, 그 주식 한주를 한번 사고 팔아 얻을 수 있는 최대 수익을 계산하는 알고리즘을
최선의 경우에 O(n)이 나오도록 작성하라

내가 작성한 코드의 시간 복잡도
-> 최선의 경우 : O(n)
-> 최악의 경우 : O(n^2)

손해(음수 결과값)을 가정하지 않는 경우 더 간단하게 작성 가능함
*/

const getMaxIndex = (arr, s) => {
  let maxValue = -1;
  let resultIndex = -1;
  for (let i = s; i < arr.length; i++) {
    if (arr[i] > maxValue) {
      maxValue = arr[i];
      resultIndex = i;
    }
  }
  return resultIndex;
};

// 최선의 경우 O(n), 최악의 경우 O(n^2)
const getMaxProfit = (stockPrices) => {
  let start = 0;
  let result = 0;

  while (start < stockPrices.length - 1) {
    const maxIndex = getMaxIndex(stockPrices, start);
    for (let i = start; i < maxIndex; i++) {
      result = Math.max(result, stockPrices[maxIndex] - stockPrices[i]);
    }
    start = maxIndex + 1;
  }

  return result;
};

// 모든 경우에 O(n)
const getMaxProfitFullyOptimized = (stockPrices) => {
  let minPrice = stockPrices[0];
  let maxProfit = 0;

  for (let i = 1; i < stockPrices.length; i++) {
    const profit = stockPrices[i] - minPrice;
    if (profit > maxProfit) {
      maxProfit = profit;
    }
    if (minPrice > stockPrices[i]) {
      minPrice = stockPrices[i];
    }
  }

  return maxProfit;
};

const ex1 = [8000, 7000, 8000, 10000, 5000, 7000]; // 중간쯤
const ex2 = [1000, 2000, 3000, 4000, 5000, 10000]; // O(n)
const ex3 = [10000, 9000, 8000, 7000, 6000, 5000]; // O(n^2)

console.log(getMaxProfitFullyOptimized(ex1));
