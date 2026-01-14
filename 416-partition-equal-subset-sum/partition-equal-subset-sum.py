class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # in this case, 

        if sum(nums) % 2 != 0:
            return False
        
        cache = {0}

        target = sum(nums) // 2

        for num in nums:
            next_cache = set()
            for el in cache:
                next_cache.add(el+num)
                next_cache.add(el)
            cache = next_cache
        return True if target in next_cache else False

