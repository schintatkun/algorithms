function min(node){
    if(node){
      var current = node;
      var min = node.val;
      while(current){
        if(current.val < min){
          min = current.val;
        }
        current = current.next
      }
      return min;
    }
    return null;
  }
  