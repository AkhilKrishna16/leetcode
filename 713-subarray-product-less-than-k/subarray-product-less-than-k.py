class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        start, end = 0, 0
        prod = 1
        count = 0

        while end < len(nums):
            prod *= nums[end]
            if prod >= k:
                while prod >= k and start <= end:
                    prod //= nums[start]
                    start += 1
            
            count += 1 + (end - start)
            end += 1
        
        return count

        