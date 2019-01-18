function arrPushFront(arr, insertValue){
    for (var i=arr.length; i>0;i--){
        arr[i] = arr[i-1];
    }
    arr[0]= insertValue;
    return arr;
}
console.log(`Before : [1,2,3,4,5]`);
console.log(arrPushFront([1,2,3,4,5], 77));