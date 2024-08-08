class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # [1, 2, 3, 4]
        # [1, 1, 2, 6]
        # [24, 12, 4, 1]
        # left auxillary array and right auxillary array

        l_m = 1
        r_m = 1
        l = [0] * len(nums)
        r = [0] * len(nums)

        for i in range(len(nums)):
            j = -i - 1
            l[i] = l_m
            r[j] = r_m
            l_m *= nums[i]
            r_m *= nums[j]
        
        return [l_a*r_a for l_a, r_a in zip(l, r)]