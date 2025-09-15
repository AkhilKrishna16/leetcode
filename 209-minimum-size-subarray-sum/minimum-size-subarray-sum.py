class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        right = 0
        curr = 0
        m = float('inf')
        while left <= right and left < len(nums) and right < len(nums):
            curr += nums[right]

            while curr >= target:
                m = min(m, right - left + 1)
                curr -= nums[left]
                left += 1
            
            right += 1
        
        return 0 if m == float('inf') else m
