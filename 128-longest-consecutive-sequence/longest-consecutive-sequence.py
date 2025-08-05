class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        max_len = 0
        for num in nums:
            if num - 1 not in nums:
                y = num
                while y in nums:
                    y += 1
                max_len = max(max_len, y - num)
        
        return max_len