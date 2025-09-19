class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        m = defaultdict(int)

        for num in nums:
            m[num] += 1
        ret = 0
        for key in m:
            if m[key] == 1:
                ret += key
        
        return ret