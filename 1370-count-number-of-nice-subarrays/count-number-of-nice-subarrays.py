class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        # have a track of the number of odd numbers
        # whenever count = k, add one to count

        curr = 0
        ret = 0
        counts = defaultdict(int)
        counts[0] = 1
        for num in nums:
            curr += num % 2
            ret += counts[curr - k]
            counts[curr] += 1
        
        return ret