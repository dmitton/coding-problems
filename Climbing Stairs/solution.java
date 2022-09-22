class Solution {
    public int climbStairs(int n) {
        int[] memo = new int[n+1];
        int counter = climb(n,memo);
        return counter;
    }
    
    public int climb(int n, int[] memo){
        if(n < 0){
            return 0;
        }
        if( n == 0){
            return 1;
        }
        if(memo[n] != 0){
            return memo[n];
        }
        
        int a = climb(n-1, memo) + climb(n-2, memo);
        memo[n] = a;
        return a;
    }
    
}
