class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # have a two pointer solution, reduce from O(n^3) -> O(n^2)
        # basically, every unique value starting from index 1 and going to n - 1 (exclusive)
        # have a left pointer and a right pointer at the edges 
        # move it together based on the rules of just adding
        # make sure to sort first

        # [-1, -1, -1, 0, 1, 2]
        # 

        nums.sort()

        ret = []

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            left = i + 1
            right = len(nums) - 1

            while left < right:
                s = nums[left] + nums[right] + nums[i]
                if s < 0:
                    left += 1
                elif s > 0:
                    right -= 1
                else:
                    ret.append([nums[left], nums[right], nums[i]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]: left += 1
                    while left < right and nums[right] == nums[right + 1]: right -= 1
        return ret

                
                    
            