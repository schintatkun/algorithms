// start algorithm projects
function reverseString(str){
    var newStr = '';
    for (let i=str.length-1;i<=0;i--){
        newStr += str[i];
    }
    return newStr;
}
reverseString("Coding Dojo");