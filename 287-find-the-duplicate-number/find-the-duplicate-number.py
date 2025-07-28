class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[nums[0]]
        fast = nums[nums[nums[0]]]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                current = nums[0]
                while current != slow:
                    current = nums[current]
                    slow = nums[slow]
                return slow
        
        return -1