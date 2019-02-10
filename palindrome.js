//Stack
var letters = [];

var word = "bob";
var reversed_word = "";

// add each letters into stack
for (let i = 0; i<word.length;i++){
    letters.push(word[i]);
}

// pop off Stack in reverse order
for (let i = 0; i<word.length; i++){
    reversed_word += letters.pop();
}

if (word === reversed_word){
    console.log("It is a palindrome");
}else{
    console.log("It's NOT a palindrome.");
}