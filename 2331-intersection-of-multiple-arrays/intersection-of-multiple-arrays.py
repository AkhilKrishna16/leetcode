class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        if len(nums) <= 0:
            return []
        
        og = set(nums[0])

        for i in range(1, len(nums)):
            og = og.intersection(set(nums[i]))
        
        return sorted(list(og))