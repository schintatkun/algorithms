function myFunc(arr) {
    var total = 0; 
    var sum = 0;
            for (var num=0; num<arr.length;num++){
                total += arr[num];
            }
    
            for (var i = 0; i < arr.length; sum+=arr[i++]){
                console.log(i);
                if (sum * 2 == total - arr[i]) 
                    {return i;}
                
            }
            return -1;  
    }
    console.log("result = " + myFunc([1, 7, 3, 0, 6, 0, 5, 6]));