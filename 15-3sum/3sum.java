class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);

        // mark each current element
        // for each element, iterate using two pointers moving them concurrently
        // if the current sum with left + right + current < 0, move the left pointer by 1
        // if > 0, move the right pointer by 1
        // otherwise, add it to the list

        // to check for duplicates, if we add something we iterate until we the first distinct element for the left and right pointers
        // otherwise, for the current element, we check if we have adjacent elements and continue
        List<List<Integer>> ret = new ArrayList<>();

        for(int i = 0; i < nums.length - 2; i++) {
            if(i > 0 && nums[i] == nums[i - 1]) continue;

            int left = i + 1;
            int right = nums.length - 1;

            while(left < right) {
                int sum = nums[left] + nums[right] + nums[i];

                if(sum == 0) {
                    ret.add(Arrays.asList(nums[left], nums[right], nums[i]));

                    while(left < right && nums[left] == nums[left + 1]) left++;
                    while(left < right && nums[right] == nums[right - 1]) right--;

                    left++;
                    right--;
                } else if(sum < 0) {
                    left++;
                } else {
                    right--;
                }
            }
        }

        return ret;
    }
}