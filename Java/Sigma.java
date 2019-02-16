public class Sigma{
    public static void main(String[] args){
        System.out.print(calSigma(-1));
    }

    public static Integer calSigma(int n){
        if (n < 0){ return 0;}
        else {
            return calSigma(n-1)+n;
        }
    }
}