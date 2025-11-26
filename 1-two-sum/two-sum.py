class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}

        for i, num in enumerate(nums):
            complement = target - nums[i]
            if complement in h:
                return (h[complement], i)
            h[num] = i
        
        return [-1, -1]
