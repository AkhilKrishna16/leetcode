class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        right = [1] * len(nums)
        left = [1] * len(nums)

        x = 1
        for i in range(len(nums)):
            left[i] = x
            x *= nums[i]
        
        x = 1
        for i in range(len(nums) - 1, -1, -1):
            right[i] = x
            x *= nums[i]
        
        ret = [1] * len(nums)
        for i in range(len(ret)):
            ret[i] = left[i] * right[i]
        
        return ret