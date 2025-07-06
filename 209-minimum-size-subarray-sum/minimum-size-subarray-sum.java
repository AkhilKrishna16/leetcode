class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        // maybe if i sort it first. if i sort it, i get an ordered list. 
        // from there i can use a sliding window alg. to find the correct subarray
        // whenever we have a contiguous sum >= target then reduce the window size by
        // decrementing start pointer
        // at each point where sum >= target, just mark down the value and compare

        int minLength = Integer.MAX_VALUE;
        int currentSum = 0;
        int start = 0, end = 0;

        for(end = 0; end < nums.length; end++) {
            currentSum += nums[end];

            if(currentSum >= target) {
                while(start <= end && currentSum >= target) {
                    minLength = Math.min(minLength, end - start + 1);
                    currentSum -= nums[start];
                    start++;
                }
            } 
        }

        return minLength == Integer.MAX_VALUE ? 0 : minLength; 
    }
}