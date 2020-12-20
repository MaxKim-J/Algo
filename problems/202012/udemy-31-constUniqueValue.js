/*
implement a function called countUniqueValues, which accepts a sorted array,
and counts the unique values is the array.
There can be negative numbers in the array, but it will always be sorted.
*/


function countUniqueValues(arr) {
  if(arr.length < 2) {
      return arr.length;
  }
  
  let count = 0;
  let firstPointer = 0;
  let secondPointer = 1;

  while(secondPointer <= arr.length) {
      if(arr[firstPointer] !== arr[secondPointer]) {
          count += 1;
          firstPointer = secondPointer;
      }
      secondPointer++;
  }
  return count;
}

console.log(countUniqueValues([]));
console.log(countUniqueValues([1,2,3,4,4,4,7,7,12,12,13]));
console.log(countUniqueValues([1,1,1,1,3]));
console.log(countUniqueValues([-2, -1, -1, 0, 1]));

