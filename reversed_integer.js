//Solution 1 : It is a simple way to do.
function reversed_int_solution1(num){
    var result = '';
    //convert input num to a tring
    var numStr = num.toString();

    //reverse input string numStr
    for (let i = numStr.length-1; i>=0; i--){
        result += numStr[i];
    }
    console.log(result);
    //convert string to integer based 10
    return parseInt(result,10);
}
reversed_int_solution1(1234);


//Solution 2
//Time: O(n)  n is number of digits
//Space: O(1)
function reversed_int_solution2(inputNum){

    var result = 0;

    // In case, it is a negative input value, then make it a positive value
    var remainder = Math.abs(inputNum);

    while (remainder != 0){
       console.log("remaining value : ",remainder);

        // shifting digit by multipling 10 
        result *= 10;
        console.log(result);

        //module operator will get a last digit of remainder and add to a result        
        result += remainder%10;

        //remove the last digit of a remainder,which has already been added to a result
        //parseInt convert a value to integer, otherwise remainder/10 will become a decimal digit
        //Expalain : 123/10 = 12.3  parseInt will take care of 0.3, the result would be just 12.
        remainder = parseInt(remainder/10, 10);
    }
    //if input is a negative value, then result as a negative value.
    return inputNum < 0 ? -result: result;
}

console.log(reversed_int_solution2(-51047));