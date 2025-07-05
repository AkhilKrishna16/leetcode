class Solution {
    public double findMaxAverage(int[] nums, int k) {
        // sliding window algorithm
        // find the window where you would get the max average out of something
        int currentSum = 0;
        for(int i = 0; i < k; i++) {    
            currentSum += nums[i];
        }

        double maxAverage = (double) (currentSum) / k;
        currentSum = 0;
        for(int i = 0; i < nums.length; i++) {
            currentSum += nums[i];

            if(i > k - 1) {
                currentSum -= nums[i - k];
                maxAverage = Math.max((double)(currentSum) / k, maxAverage);
            }
        }

        return maxAverage;
    }
}