class Solution {
    public boolean isPalindrome(int x) {
        int reverse = 0;
        int rem;
        int number = x;
        while(x > 0){
            rem = x % 10;
            reverse = (reverse * 10) + rem;
            x = x/10;
        }
        
        String num = Integer.toString(number);
        String reversed = "";
        for(int i = num.length() - 1; i >= 0; i--){
            reversed += num.charAt(i);
        }
        
        
        boolean isPalindrome = true;
        for(int i = 0; i < num.length();++i){
            if(num.charAt(i) == reversed.charAt(i)){
                isPalindrome = true;
                
            }
            else{
                isPalindrome = false;
                return false;
            }
        }
        return true;
    }
}
