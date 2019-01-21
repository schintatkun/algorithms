function arrInsertAt(arr,index, val){
    if((index <0) || (index> arr.length-1)) {
        return ;
    }else {
        // do ....
        var nextTemp;
        var a = arr[index];
        // console.log('tempvariable = '+temp);
        arr[index] = val;
        // arr[index+1]=temp;
    
        for (var i = index+1; i < arr.length+1; i++) {
            console.log('Loop i value = '+i);

        }
    }
    console.log(arr);
}
arrInsertAt([1,2,3,4,5,6,7],0, "hello");