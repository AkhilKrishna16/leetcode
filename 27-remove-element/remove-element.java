class Solution {

    public static void swap(int[] nums, int first, int second) {
        int temp = nums[first];
        nums[first] = nums[second];
        nums[second] = temp;
    }

    public int removeElement(int[] nums, int val) {
        // front pointer marks where the accepted values current insert index is
        // back pointer marks where the rejected values current insert index is 

        int front = 0;
        int back = nums.length - 1;
        int count = 0;

        while(front <= back) {
            if(nums[front] == val) {
                swap(nums, front, back);
                back--;
                count++;
            } else {
                front++;
            }
        }

        return back + 1;
    }
}