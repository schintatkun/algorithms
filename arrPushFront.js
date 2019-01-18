function arrPushFront(arr, insertValue){
    for (var i=arr.length; i>0;i--){
        arr.length = arr.length-1;
    }
    arr[0]= insertValue;
    return arr;
}
arrPushFront([1,2,3,4,5], 77);