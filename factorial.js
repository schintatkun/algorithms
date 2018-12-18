function fastFactorial(num){
  if(num < 0){return 0;}
  var result = num;
  while(num > 1){
    num--;
    result *= num;
    
   }
  return result;
}
console.log(fastFactorial(5));