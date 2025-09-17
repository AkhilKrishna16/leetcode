class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        freqs = defaultdict(int)

        for a in nums:
            for num in a:
                freqs[num] += 1

        ret = []
        for key in freqs:
            if freqs[key] == len(nums):
                ret.append(key)
        
        return sorted(ret)