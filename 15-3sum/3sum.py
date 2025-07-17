class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort the array
        # have a start, middle, and end
        # we iterate middle onwards through the list
        # we have start and end, whenever the target is less than sum, move the right pointer down
        # and vice versa, 
        nums = sorted(nums)
        ret = []
        
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                if nums[right] + nums[left] + nums[i] == 0:
                    ret.append([nums[right], nums[left], nums[i]])

                    # move pointers to avoid duplicates
                    left += 1
                    right -= 1
                    while(left < right and nums[left] == nums[left - 1]): left += 1
                    while(right > left and nums[right] == nums[right + 1]): right -= 1
                elif nums[right] + nums[left] + nums[i] > 0:
                    right -= 1
                else:
                    left += 1
        
        return ret


        
