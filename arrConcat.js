function arrConcat(arr1,arr2){
    var newArray = [];
    for(var first = 0; first < arr1.length; first++){
      newArray[first] = arr1[first];
    }
    for(var second = 0; second < arr2.length; second++){
      newArray[newArray.length] = arr2[second];
    }
    return newArray;
  }
  console.log(arrConcat([],[67,87,78,98]));