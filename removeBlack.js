function removeBlanks(str){
    var new_str = "";
    for(var i = 0; i < str.length; i++){
      if(str[i] != " "){
        new_str += str[i];
      }
    }
    return new_str;
  }
  
  console.log(removeBlanks(" test Test test tset "));