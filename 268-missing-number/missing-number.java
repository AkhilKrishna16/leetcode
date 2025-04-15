class Solution {
    public int missingNumber(int[] nums) {
        int sum = 0;
        int expected = (nums.length * nums.length + nums.length) / 2;
        for(int i = 0; i < nums.length; i++) {
            sum += nums[i];
        }

        return expected - sum;
    }
}