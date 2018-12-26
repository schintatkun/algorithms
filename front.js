function length(firstNode){
  if(firstNode){
    var current = firstNode;
    var nodeSize = 1;
    while(current){
      if(current.next != null){
        current = current.next
        nodeSize += 1;
      }
    }
    return nodeSize;
  }
  return null;
}

console.log(length(node1));