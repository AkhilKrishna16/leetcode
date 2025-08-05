class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        max_length = 0
        for num in nums:
            y = num
            if y - 1 not in nums:
                while y in nums:
                    y += 1
                max_length = max(max_length, y - num)
        
        return max_length