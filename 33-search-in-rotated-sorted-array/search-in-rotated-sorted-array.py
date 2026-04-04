class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # we have to find the current value's "position" respective to the ends 
        # so for instance, if the `right` index value is greater than the current value
        # then if the curr < target < right, then we search the right side. else search the left side 
        # however, if the `right` index value is less than the current value
        # then if the target > curr, search the right side. else the left side 

        #   6 7 8 0 1 2 3 4 5

        left = 0
        right = len(nums) - 1

        while left < right:
            curr = (left + right) // 2
            if nums[curr] == target:
                return curr
            if nums[curr] < nums[right]:
                if nums[curr] < target <= nums[right]:
                    left = curr + 1
                else:
                    right = curr - 1
            elif nums[curr] > nums[right]:
                if target <= nums[right] or target > nums[curr]:
                    left = curr + 1
                else:
                    right = curr - 1
        if nums[left] == target:
            return left
        return -1