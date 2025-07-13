class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}

        for i, num in enumerate(nums):
            m[num] = i
        
        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in m and i != m[complement]:
                return [m[complement], i]
        
        return []