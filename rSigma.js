function rSigma(num) {
    if (num < 1) return 0;
    return rSigma(num-1) + num;
}

console.log(rSigma(5));