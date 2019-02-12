function permutationStr(str, prefix){
    if (str.length == 0){
        console.log(prefix);
    }else {
        for (let i =0; i<str.length; i++){
            var rem = str.subString(0,i) + str.subString(i+1);
            permutationStr(rem, prefix+str.charAt(i));
        }
    }
}