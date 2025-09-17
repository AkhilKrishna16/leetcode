class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums = sorted(nums)
        j = 0
        for i, num in enumerate(nums):
            if nums[i] != j:
                return j
            j += 1
        
        return j

        
