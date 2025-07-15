class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # [1, 2, 3, 4, 5]
        ret = [0] * len(nums)

        left, right = 0, len(nums) - 1
        i = len(nums) - 1

        while left <= right:
            if nums[left] ** 2 <= nums[right] ** 2:
                ret[i] = nums[right] ** 2
                right -= 1
            else:
                ret[i] = nums[left] ** 2
                left += 1
            
            i -= 1
        
        return ret