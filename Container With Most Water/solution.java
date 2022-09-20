class Solution {
    public int maxArea(int[] height) {
        int max = 0;
        int leftCounter = 0;
        int rightCounter = height.length - 1;
        while(leftCounter != rightCounter){
            int width = (height[leftCounter] < height[rightCounter]) ? height[leftCounter] : height[rightCounter];
            int length = rightCounter - leftCounter;
            int area = width * length;
            if(area > max){
                max = area;
            }
            if(height[rightCounter] < height[leftCounter]){
                rightCounter -= 1;
            }
            else{
                leftCounter += 1;
            }
        }
        return max;
    }
}
