function shiftArray(arr){
    for (var i; i<arr.length; i++){
        arr[i-1]=arr[i];
    }
        arr.pop();
}