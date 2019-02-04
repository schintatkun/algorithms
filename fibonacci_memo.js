function fib_memo(n, memo){
    if (memo[n] != null){
        return memo[n];
    }
    if (n==1 || n==2){
        return 1;
    } else {
        result = fib_memo(n-2)+fib_memo(n-1);
        memo[n] = result;
    }
    return result;
}

console.log(fib_memo(5));