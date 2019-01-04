function average(node){
  if(node){
    var current = node;
    var length = 0;
    var sum = 0;
    while(current){
      sum += current.val;
      current = current.next;
      length += 1; 
    }
    return sum/length;
  }
}