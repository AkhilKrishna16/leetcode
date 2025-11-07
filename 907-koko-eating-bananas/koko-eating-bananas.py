class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # O(log(piles) * h)
        
        # for some value k (binary search on this) (low = 0, high = max(piles))
        # find the min k by checking whether the total hours taken to eat
        # everything in the piles < h

        def check(k):
            hours_taken = 0
            for pile in piles:
                hours_taken += ceil(pile / k)
            return hours_taken <= h
        
        low, high = 1, max(piles)
        while low <= high:
            k = (low + high) // 2
            if check(k): # we can eat everything
                high = k - 1
            else:
                low = k + 1
        return low