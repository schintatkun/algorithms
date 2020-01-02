function arraySum(arr) {
  return arr.reduce((a, b) => a + b);
}

console.log(arraySum([1, 2, 3, 4, 5]));
console.log(arraySum([2, 4, 6, 8, 10, 12]));
