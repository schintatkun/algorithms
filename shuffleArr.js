function shuffle(arr){
  for(var i = 0; i < arr.length; i++){
    var pos = Math.floor(Math.random() * Math.floor(arr.length));
    var tmp = arr[i];
    arr[i] = arr[pos];
    arr[pos] = tmp;
  }
  return arr;
}

console.log(shuffle([1,2,3,4,5,6,7,8,9,10]));