class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        RED = 0
        WHITE = 1
        BLUE = 2

        # partition such that red goes in the front and blue marker goes in teh back
        # 

        curr = 0
        left = 0
        right = len(nums) - 1

        while curr <= right and left < right:
            if nums[curr] == RED:
                nums[curr], nums[left] = nums[left], nums[curr]
                left += 1
                curr = left
            elif nums[curr] == BLUE:
                nums[curr], nums[right] = nums[right], nums[curr]
                right -= 1
            else:
                curr += 1
        


        