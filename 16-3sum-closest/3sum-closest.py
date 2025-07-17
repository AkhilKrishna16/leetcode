class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        ret = 0

        # same as regular 3Sum solution except every single time, just check whether it is in fact
        # the closest distance to the target by having a closestValue marker

        closestValue = float('inf')
        newSum = 0

        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                currentSum = nums[left] + nums[right] + nums[i]
                if closestValue > abs(target - currentSum):
                    closestValue = abs(target - currentSum)
                    newSum = currentSum
                
                if target < currentSum:
                    right -= 1
                elif target > currentSum:
                    left += 1
                else:
                    left += 1
                    right -= 1
        return newSum 