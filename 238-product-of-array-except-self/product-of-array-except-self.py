class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # right = [1] * len(nums)
        # left = [1] * len(nums)
        ret = [1] * len(nums)
        x = 1
        for i in range(len(nums)):
            ret[i] *= x
            x *= nums[i]
        
        x = 1
        for i in range(len(nums) - 1, -1, -1):
            ret[i] *= x
            x *= nums[i]
        
        return ret