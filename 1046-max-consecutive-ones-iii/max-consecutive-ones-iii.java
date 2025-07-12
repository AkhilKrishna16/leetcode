class Solution {
    public int longestOnes(int[] nums, int k) {
        // have a window of at least k length (if < k length, add the character regardless)
        // continue have a count of the number of 1s, if length - max_count > k, run a while loop
        // to reduce the start pointer

        int start = 0, end = 0;
        int ones_count = 0;
        int maxLength = Integer.MIN_VALUE;
        for(end = 0; end < nums.length; end++) {
            if(nums[end] == 1) {
                ones_count++;
            }

            if(end - start + 1 - ones_count > k) {
                // run a while loop to reduce the start pointer
                while(end - start + 1 - ones_count > k) {
                    ones_count -= nums[start];
                    start++;
                }
            }

            maxLength = Math.max(end - start + 1, maxLength);
        }
        
        return maxLength;
    }
}