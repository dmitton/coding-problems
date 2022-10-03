class Solution {
    public int search(int[] nums, int target) {
        int min = 0;
        int max = nums.length - 1;
        int mid;
        
        
        while(min <= max){
            mid = min + (max - min) / 2;
            if(target == nums[mid]){
                return mid;
            }
            else{
                if(target > nums[mid]){
                    min = min + 1;
                }
                else if(target < nums[mid]){
                    max = max - 1;
                }
            }
        }
        return -1;
        
    }
}
