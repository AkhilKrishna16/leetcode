class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        # brute force: multiply spells[i] by everything in potions for every i
        # O(n * m), n = spells.length, m = potions.length
        # perform binary search for every one of the spells on the potions array
        # sort the array for potions and keep finding the middle until we get a 
        # combination where spells[i] * potions[i] >= success
        # then add everything from i onwards till end, so n - i
        res = [0] * len(spells)
        potions.sort()
        for i in range(len(spells)):
            low, high = 0, len(potions) - 1
            while low <= high:
                mid = (low + high) // 2
                if potions[mid] * spells[i] >= success:
                    high = mid - 1
                elif potions[mid] * spells[i] < success:
                    low = mid + 1
            res[i] = len(potions) - low
        return res