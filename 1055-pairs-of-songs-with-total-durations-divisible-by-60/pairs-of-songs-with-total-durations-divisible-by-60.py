class Solution:
    def numPairsDivisibleBy60(self, times: List[int]) -> int:
        count = defaultdict(int)
        pairs = 0
        for t in times:
            mod = t % 60
            if mod == 0:
                pairs += count[0]
            else:
                pairs += count[60 - mod]
            count[mod] += 1
                
        
        return pairs