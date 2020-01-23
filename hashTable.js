// Hash Table

// "string" that we want to hash
// "max" parameter is number of buckets that's using in the hash table to store values
var hash = (string, max) => {
  var hash = 0;
  for (var i = 0; i < string.length; i++) {
    hash += string.charCodeAt(i);
  }
  //return the remainder
  return hash % max;
};
