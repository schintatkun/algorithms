function Fib(n) {
    let num = Math.floor(n);
    if (num <= 0) return 0;
    if (num === 1) return 1;

    return Fib(num - 1) + Fib(num - 2);
}
