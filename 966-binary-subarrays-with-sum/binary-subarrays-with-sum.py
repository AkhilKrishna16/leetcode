class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        m = defaultdict(int)
        m[0] = 1
        curr_sum = 0
        ret = 0
        for num in nums:
            curr_sum += num
            if (curr_sum - goal) in m:
                ret += m[curr_sum - goal]
            m[curr_sum] += 1
        
        return ret
