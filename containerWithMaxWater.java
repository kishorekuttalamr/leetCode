class Solution {
    public int maxArea(int[] height) {
        int minHeight = height[0];
        int maxHeight = height[height.length - 1];
        int minIndex = 0;
        int maxIndex = height.length - 1;
        
        if (maxHeight < minHeight) {
            minHeight = maxHeight;
            minIndex = maxIndex;
            maxHeight = height[0];
            maxIndex = 0;
        }
        
        int width = height.length - 1;
        int maxArea = width * minHeight;
        
        while (width > 0) {
            int index = minIndex;
            
            while (height[index] <= minHeight) {
                if (minIndex < maxIndex) {
                    index++;
                } else {
                    index--;
                }
                width--;
                
                if (width < 1) {
                    break;
                }
            }
            
            if (height[index] > maxHeight) {
                minHeight = maxHeight;
                minIndex = maxIndex;
                maxIndex = index;
                maxHeight = height[index];
            } else {
                minIndex = index;
                minHeight = height[index];
            }
            
            maxArea = Math.max(maxArea, width * minHeight);
        }
        
        return maxArea;
    }
    
    public static void main(String[] args) {
        Solution solution = new Solution();
        
        int[] height = {1, 8, 6, 2, 5, 4, 8, 3, 7};
        int maxContainerArea = solution.maxArea(height);
        
        System.out.println("Maximum area of the container: " + maxContainerArea);
    }
}
