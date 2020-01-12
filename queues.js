// Queues

function Queue() {
  collection = [];
  this.print = function() {
    console.log(collection);
  };
  this.enqueue = function(element) {
    collection.push(element);
  };
  this.dequeue = function() {
    collection.shift();
  };
  this.front = function() {
    return collection[0];
  };
  this.size = function() {
    return collection.length;
  };
  this.isEmpty = function() {
    return coolection.length === 0;
  };
}
var q = new Queue();
q.enqueue("A");
q.enqueue("B");
q.enqueue("C");
q.print();
q.dequeue();
console.log("This is a front element : ", q.front());
q.print();
