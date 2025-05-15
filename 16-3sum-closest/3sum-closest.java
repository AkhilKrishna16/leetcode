class Solution {
    public int threeSumClosest(int[] nums, int target) {
        int sum = 0;
        int closest = Integer.MAX_VALUE;
        int ret = 0;

        Arrays.sort(nums);

        for(int i = 0; i < nums.length - 2; i++) {
            int left = i + 1;
            int right = nums.length - 1;

            while(left < right) {
                sum = nums[i] + nums[left] + nums[right];

                if(sum == target) {
                    return sum;
                }

                if(Math.abs(sum - target) < closest) {
                    ret = sum;
                    closest = Math.abs(sum - target);
                }

                if(sum < target) {
                    left++;
                } else if (sum > target) {
                    right--;
                }
            }
        }

        return ret; 
    }
}