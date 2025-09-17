class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        counts = defaultdict(int)
        counts[0] += 1
        
        curr = 0
        ret = 0
        for num in nums:
            curr += num
            ret += counts[curr - k]
            counts[curr] += 1
        return ret