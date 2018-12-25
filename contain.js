function contains(firstNode,value){
    var current = firstNode;
    while(current){
      if(current.val == value){
        return true;
      }
      current = current.next
    }
    return false;
  }
  
  console.log(contains(node1,6));