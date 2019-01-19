function arrPopFront(arr){
    var result = arr[0];
    var newArr = [];
    for (var i=1;i<arr.length;i++){
        newArr[i-1] = arr[i];
    }
    // for (var i=1; i<=arr.length;i++){
    //     arr[i-1] = arr[i];
    // }
    // console.log('last index = '+arr[i]);
    // console.log(arr);
    console.log('Array[0] = '+ result);
    console.log(newArr);
    return result;
}
arrPopFront([1,2,3,4,5,6]);