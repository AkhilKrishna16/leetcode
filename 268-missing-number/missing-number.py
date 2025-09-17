class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums = set(nums)
        n = len(nums) + 1
        for i in range(n + 1):
            if i not in nums:
                return i
        
