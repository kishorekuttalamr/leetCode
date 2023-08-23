class Solution {
    public int maxArea(int[] height) {
        int minHeight = height[0];
        int maxHeight = height[height.length - 1];
        int minIndex = 0;
        int maxIndex = height.length - 1;
        
        // Swap min and max height if necessary to ensure the starting state has a taller line on the right
        if (maxHeight < minHeight) {
            minHeight = maxHeight;
            minIndex = maxIndex;
            maxHeight = height[0];
            maxIndex = 0;
        }
        
        int width = height.length - 1;
        int maxArea = width * minHeight; // Initialize maxArea with the initial width and minHeight
        
        // Continue loop while there's still width left to consider
        while (width > 0) {
            int index = minIndex;
            
            // Move index to find the next line that is taller than or equal to minHeight
            while (height[index] <= minHeight) {
                if (minIndex < maxIndex) {
                    index++;
                } else {
                    index--;
                }
                width--;
                
                // Break the loop if there's no more width to consider
                if (width < 1) {
                    break;
                }
            }
            
            // Update minHeight and indices if a taller line is found
            if (height[index] > maxHeight) {
                minHeight = maxHeight;
                minIndex = maxIndex;
                maxIndex = index;
                maxHeight = height[index];
            } else {
                minIndex = index;
                minHeight = height[index];
            }
            
            // Update maxArea if a larger area is found
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
