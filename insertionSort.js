function insertionSort(arr) {
  for (let i = 1; i < arr.length; i++) {
    let current = arr[i];
    let j = i - 1;
    while (j >= 0 && arr[i] > current) {
      arr[j + 1] = arr[j];
      j--;
    }
    arr[j + 1] = current;
  }
  console.log(arr);
  return arr;
}
console.log("Sort Empty Array : ", insertionSort([]));
console.log("Sort array that has a single value: ", insertionSort([2]));
console.log(insertionSort([2, 10, 22, 5, 3, 0, 102, 76]));
