function powerof2(n){
    var num = parseInt(n);
    if (num < 1){
        console.log('Your input number is less than 1');
        return 0;
    } else if (num === 1) {
        console.log("1");
        return 1;
    } else {
        var prev = powerof2(num/2);
        var curr = prev*2;
        console.log(curr);
        return curr;
    }
}

powerof2(50);