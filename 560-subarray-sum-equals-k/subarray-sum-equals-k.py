class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        freq_runs = defaultdict(int)
        running_count = 0
        ret = 0
        freq_runs[0] = 1
        for num in nums:
            running_count += num
            if running_count - k in freq_runs:
                ret += freq_runs[running_count - k]
            
            freq_runs[running_count] += 1
        
        return ret