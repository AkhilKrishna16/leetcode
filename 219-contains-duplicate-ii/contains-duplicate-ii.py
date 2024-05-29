class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if not nums or len(nums) == 1:
            return False

        f = {}

        for i, val in enumerate(nums):
            if val in f:
                if i - f[val] <= k:
                    return True
            f[val] = i

        return False 