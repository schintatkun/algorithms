function nodeClass(value){
  this.val = value;
  this.next = null;
}

function removeFront(firstNode){
    if(firstNode){
      var newNode = firstNode.next;
      firstNode.next = null;
      return newNode;
    }
    return null;
  }

node1 = new nodeClass(1);
node2 = new nodeClass(2);
node1.next = node2;
console.log(removeFront(node1));