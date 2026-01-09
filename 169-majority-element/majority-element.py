class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        m = Counter(nums)

        for k in m:
            if m[k] > len(nums) // 2:
                return k
        
        return -1