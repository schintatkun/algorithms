// Hash Table

// "string" that we want to hash
// "max" parameter is number of buckets that's using in the hash table to store values
var hash = (string, max) => {
  var hash = 0;
  for (var i = 0; i < string.length; i++) {
    hash += string.charCodeAt(i);
  }
  //return the remainder, which is an index in array
  return hash % max;
};

let HashTable = function() {
  let storage = [];
  const storageLimit = 4;

  // print all items in storage array
  this.print = function() {
    console.log(storage);
  };

  // add item function
  this.add = function(key, value) {
    // find an index of array by running through hash function
    var index = hash(key, storageLimit);

    // if nothing in this index of storage array, then set key && value pairs
    // to this index
    if (storage[index] === undefined) {
      storage[index] = [[key, value]];
    } else {
      var inserted = false;

      // go through all index if the key already exists.
      for (var i = 0; i < storage[index].length; i++) {
        // if key already exists, then set a new value here.
        if (storage[index][i][0] === key) {
          storage[index][i][1] = value;
          inserted = true;
        }
      }
      // if the key does not exist, then push in key & value into storage array
      if (inserted === false) {
        storage[index].push([key, value]);
      }
    }
  };
  // remove item function
  this.remove = function(key) {
    var index = hash(key, storageLimit);
    if (storage[index].length === 1 && storage[index][0][0] === key) {
      delete sotrage[index];
    } else {
      for (var i = 0; i < storage[index]; i++) {
        if (storage[index][i][0] === key) {
          delete storage[index][i];
        }
      }
    }
  };
};
