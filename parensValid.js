function parensValid(str){
    var arr = [];
    for(var i=0; i<str.length; i++){
        switch(str[i]) {
        case "(":
            arr.push(str[i]);   
            break;
        case ")":
            if (arr[arr.length-1] === "("){
                arr.pop();
            } else {
                return false;
            }
            break;
        default:
            continue;
        }
    }
    return true;
}

function bracesValid(str){
    var arr = [];
    obj = {
        ")":"(",
        "}":"{",
        "]":"["
    }
    for(var i=0; i<str.length; i++){
        switch(str[i]) {
            case "(": 
            case "{": 
            case "[":
                arr.push(str[i]);   
                break;
            case ")": 
            case "}": 
            case "]":
                if(obj[str[i]] === arr[arr.length-1]){
                    arr.pop();
                } else {
                    return false;
                }
                break;
            default:
                continue;
        }
    }
    if (arr.length) return false; 
    return true;
}