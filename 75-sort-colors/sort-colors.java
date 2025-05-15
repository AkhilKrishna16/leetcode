class Solution {

    public static void swap(int[] nums, int first, int second) {
        int temp = nums[first];
        nums[first] = nums[second];
        nums[second] = temp;
    }

    public void sortColors(int[] nums) {
        int redMarker = 0;
        int blueMarker = nums.length - 1;
        int marker = 0;

        while(marker <= blueMarker) {
            if(nums[marker] == 0) {
                swap(nums, marker, redMarker);
                redMarker++;
                marker = redMarker;
            } else if(nums[marker] == 2) {
                swap(nums, marker, blueMarker);
                blueMarker--;
            } else {
                marker++; 
            }
        }
    }
}