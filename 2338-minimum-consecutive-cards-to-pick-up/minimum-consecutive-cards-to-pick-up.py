class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        # mark the most recent index of the specific number that you are on
        # record the minimum and mark that down

        ret = float('inf')
        m = defaultdict(int)

        for i in range(len(cards)):
            if cards[i] in m:
                ret = min(ret, i - m[cards[i]] + 1)
            m[cards[i]] = i
        
        return -1 if ret == float('inf') else ret