class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        m = defaultdict(int)
        left = 0
        ret = 0

        for right in range(len(nums)):
            m[nums[right]] += 1
            while m[nums[right]] > k and left < right:
                m[nums[left]] -= 1
                left += 1
            ret = max(ret, right - left + 1)
        
        return ret
                