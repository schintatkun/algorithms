function nodeClass(value){
    this.val = value;
    this.next = null;
  }
  
  node1 = new nodeClass(1);
  
  function addFront(firstNode, value){
    var newNode = new nodeClass(value);
    newNode.next = firstNode;
    return newNode;
  }
  
  console.log(addFront(node1,2));
  